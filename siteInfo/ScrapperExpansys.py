import scrapy
from DatabaseConnection import DataBaseConnection


class ExpansysSpider(scrapy.Spider):
    name = "expansys"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatusInfo = response.css('div[id="product"] div[id="prod_head"] ul.details li[id="stock"]::attr("content")').extract_first();
        stockStatus = "Unknown"
        if stockStatusInfo is not None:
            if 'in_stock' in stockStatusInfo:
                stockStatus = 'In Stock';
            else:
                stockStatus = 'Out of Stock';

        title = response.css('div[id="product"] div[id="title"] h1::text').extract_first()
        priceString = response.css('div[id="product"] div[id="prod_head"] p[id="price"] span[itemprop="price"]::text').extract_first()
        price = None;
        if priceString is not None:
            price = priceString[1::].replace(',', '')
        db.insertData(title, price, stockStatus, self.name)
