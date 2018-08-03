import scrapy
from DatabaseConnection import DataBaseConnection


class AsianicSpider(scrapy.Spider):
    name = "asianic"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatus = 'Unknown';
        title = response.css('h1::text').extract_first()
        priceString = response.css('span.productdetail_price::text').extract()
        price = None
        if priceString != [] and len(priceString) > 1:
            price = priceString[1].replace(',', '').strip()
        db.insertData(title, price, stockStatus, self.name)