import scrapy
from DatabaseConnection import DataBaseConnection


class TakatackSpider(scrapy.Spider):
    name = "takatack"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatusField = response.css('div.product-main-info div.stocks-qty div.stocks span.stock-count::text').extract_first()
        stockStatus = 'Unknown';
        if stockStatusField is not None:
            if int(stockStatusField) > 0:
                stockStatus = 'In Stock';
            else:
                stockStatus = 'Out of Stock';

        title = response.css('div.product-main-info h1.product-title::text').extract_first()
        price = response.css('div.product-main-info div.price-detail span.price span[id="finalPrice"]::text').extract_first()
        db.insertData(title, price, stockStatus, self.name)
