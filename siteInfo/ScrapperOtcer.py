import scrapy
from DatabaseConnection import DataBaseConnection


class OtcerSpider(scrapy.Spider):
    name = "otcer"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return
        stockStatus = 'Unknown';
        title = response.css('h1.product_title::text').extract_first()
        price = response.css('p.price span.electro-price span::text').extract()[1].replace(',', '')
        db.insertData(title, price, stockStatus, self.name)
