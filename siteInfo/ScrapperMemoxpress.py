import scrapy
from DatabaseConnection import DataBaseConnection


class MemoxpressSpider(scrapy.Spider):
    name = "memoxpress"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatus = 'Unknown';
        title = response.css('h1.productname span::text').extract_first()
        if title is None:
            title = response.css('h1.product-title::text').extract_first()
        priceString = response.css('div.productpageprice::text').extract()
        price = None;
        if priceString != []:
            price = priceString[len(priceString) - 1][2::].strip().replace(',', '')
        elif response.css('span[id="finalPrice"]::text').extract_first() is not None:
            price = response.css('span[id="finalPrice"]::text').extract_first().replace(',', '')
        db.insertData(title, price, stockStatus, self.name)
