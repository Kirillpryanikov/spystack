import scrapy
from DatabaseConnection import DataBaseConnection


class WidgetcitySpider(scrapy.Spider):
    name = "widgetcity"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        price = None;
        stockStatus = 'Unknown'
        stockStatusInfo = response.xpath('//ul[@class="list-unstyled"]/li[contains(text(), "Availability:")]/span/text()').extract_first();
        if stockStatusInfo is not None:
            if 'In Stock' in stockStatusInfo:
                stockStatus = 'In Stock';
            else:
                stockStatus = 'Out of Stock';

        title = response.css('h1.product-name::text').extract_first()
        priceString = response.css('ul.price-product li span::text').extract_first()
        if priceString is not None:
            price = priceString[1::].replace(',', '')
        db.insertData(title, price, stockStatus, self.name)
