import scrapy
from DatabaseConnection import DataBaseConnection


class VillmanSpider(scrapy.Spider):
    name = "villman"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatus = 'Unknown';
        title = response.css('div[id="middle-section"] h1[id="h1productname"]::text').extract_first()
        priceString = response.css('div[id="middle-section"] div[id="product_details_right"] td.price_maroon::text').extract_first()
        price = None;
        if priceString is not None:
            price = priceString.strip().replace(',', '')
        db.insertData(title, price, stockStatus, self.name)
