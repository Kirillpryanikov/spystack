import scrapy
from DatabaseConnection import DataBaseConnection


class SavenearnSpider(scrapy.Spider):
    name = "savenearn"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatusInfo = response.css('div.summary div.single-product-price link[itemprop="availability"]::attr("href")').extract_first();
        stockStatus = 'Out of Stock';
        if stockStatusInfo is not None:
            if 'InStock' in stockStatusInfo:
                stockStatus = 'In Stock';
        title = response.css('div.summary h1.product-title::text').extract_first()
        price = response.css('div.summary div.single-product-price meta[itemprop="price"]::attr("content")').extract_first()
        db.insertData(title, price, stockStatus, self.name)
