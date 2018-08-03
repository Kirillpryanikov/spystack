import scrapy
from DatabaseConnection import DataBaseConnection


class ElnstoreSpider(scrapy.Spider):
    name = "elnstore"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatus = 'Unknown';

        title = response.css('div.product-name h1::text').extract_first()
        price = response.css('div.price-box span.price::attr("content")').extract_first()
        db.insertData(title, price, stockStatus, self.name)

