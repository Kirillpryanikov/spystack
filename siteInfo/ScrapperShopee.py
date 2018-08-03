import scrapy
from DatabaseConnection import DataBaseConnection


class ShopeeSpider(scrapy.Spider):
    name = "shopee"

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
        title = response.css('h1.shopee-product-info__header__text::text').extract_first()
        price = response.css('div.shopee-product-info__header__real-price::text').extract_first()[1::].replace(',', '')
        db.insertData(title, price, stockStatus, self.name)
