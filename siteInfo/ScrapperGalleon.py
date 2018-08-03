import scrapy
from DatabaseConnection import DataBaseConnection


class GalleonSpider(scrapy.Spider):
    name = "galleon"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatus = 'Out of Stock';
        title = response.css('div.detail-container div.product-title h1.product-name::text').extract_first()
        priceString = response.css('div.detail-container div.buy-now div.product-srp-price span[itemprop="price"]::text').extract_first()
        price = None;
        if priceString is not None:
            price = priceString[2::].replace(',', '')
            stockStatus = 'In Stock';
        db.insertData(title, price, stockStatus, self.name)
