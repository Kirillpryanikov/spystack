import scrapy
from DatabaseConnection import DataBaseConnection


class AnsonSpider(scrapy.Spider):
    name = "anson"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatusInfo = response.css('div.product div.summary div[itemprop="offers"] link[itemprop="availability"]::attr("href")').extract_first();
        stockStatus = 'Unknown';
        if stockStatusInfo is not None:
            if 'InStock' in stockStatusInfo:
                stockStatus = 'In Stock';
            else:
                stockStatus = 'Out of Stock';

        title = response.css('div.product div.summary h1.product_title::text').extract_first()
        price = response.css('div.product div.summary div[itemprop="offers"] meta[itemprop="price"]::attr("content")').extract_first()
        db.insertData(title, price, stockStatus, self.name)
