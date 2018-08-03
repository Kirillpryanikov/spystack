import scrapy
from DatabaseConnection import DataBaseConnection


class ArgomallSpider(scrapy.Spider):
    name = "argomall"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatusInfo = response.css('div.product-shop div.price-stock div.price-box link[itemprop="availability"]::attr("href")').extract_first();
        stockStatus = 'Unknown';
        if stockStatusInfo is not None:
            if 'InStock' in stockStatusInfo:
                stockStatus = 'In Stock';
            else:
                stockStatus = 'Out of Stock';

        title = response.css('div.product-shop div.product-name h1::text').extract_first()
        price = response.css('div.product-shop div.price-stock div.price-box meta[itemprop="price"]::attr("content")').extract_first()
        db.insertData(title, price, stockStatus, self.name)
