import scrapy
from DatabaseConnection import DataBaseConnection


class EmcorSpider(scrapy.Spider):
    name = "emcor"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatus = 'Unknown';
        title = response.css('div.summary-container h2.product_title::text').extract_first()
        price = response.css('div.summary-container p.price span.amount::text').extract_first().replace(',', '')
        db.insertData(title, price, stockStatus, self.name)