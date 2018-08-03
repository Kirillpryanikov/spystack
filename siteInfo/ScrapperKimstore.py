import scrapy
from DatabaseConnection import DataBaseConnection


class KimstoreSpider(scrapy.Spider):
    name = "kimstore"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatusInfo = response.css('div.product-info-main div.stock span::text').extract_first();
        stockStatus = 'Unknown';
        if stockStatusInfo is not None:
            if 'In stock' in stockStatusInfo:
                stockStatus = 'In Stock';
            else:
                stockStatus = 'Out of Stock';

        title = response.css('div.product-info-main div.product-info-stock-sku div.sku div.value::text').extract_first()
        price = response.css('div.product-info-main div.product-info-price span.price-wrapper::attr("data-price-amount")').extract_first()
        db.insertData(title, price, stockStatus, self.name)

