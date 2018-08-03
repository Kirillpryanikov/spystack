import scrapy
from DatabaseConnection import DataBaseConnection


class LazadaSpider(scrapy.Spider):
    name = "lazada"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatus = 'Unknown';
        title = response.css('h2.pdp-mod-section-title::text').extract_first()
        price = response.css('span.pdp-price::text').extract_first()[1::]
        db.insertData(title, price, stockStatus, self.name)
