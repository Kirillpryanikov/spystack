import scrapy
from DatabaseConnection import DataBaseConnection


class BigbentaSpider(scrapy.Spider):
    name = "bigbenta"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatusInfo = response.css('div.desc_con span.variant_hidden p::text').extract();
        stockStatus = 'Out of Stock';
        for stockStatusInfoElement in stockStatusInfo:
            if stockStatusInfoElement.find("Available Stocks:") >= 0:
                stockStatus = 'In Stock';

        title = response.css('div.title_page h1::text').extract_first()
        price = response.css('div.desc_con span.variant_hidden div.dim_and_w::attr("data-price")').extract_first()
        db.insertData(title, price, stockStatus, self.name)
