import scrapy
from DatabaseConnection import DataBaseConnection


class GoodsSpider(scrapy.Spider):
    name = "goods"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatusInfo = response.css('div.product-top-right div.product-quantity span.stock').extract_first();
        if stockStatusInfo is not None:
            stockStatus = 'In Stock';
        else:
            stockStatus = 'Out of Stock';

        title = response.css('div.product-title h1::text').extract_first()
        priceSrting = response.css('div.product-top-right span[id="price-num"]::text').extract_first()
        price = None;
        if priceSrting is not None:
            price = priceSrting[1::].replace(',', '');
        db.insertData(title, price, stockStatus, self.name)

