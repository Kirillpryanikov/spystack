import scrapy
from DatabaseConnection import DataBaseConnection


class PounditSpider(scrapy.Spider):
    name = "poundit"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatus = 'Unknown';
        title = response.css('h1.product_name[itemprop="name"]::text').extract_first()
        price = response.css('span[itemprop="price"]::attr("content")').extract_first()
        db.insertData(title, price, stockStatus, self.name)

