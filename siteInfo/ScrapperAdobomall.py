import scrapy
from DatabaseConnection import DataBaseConnection


class AdobomallSpider(scrapy.Spider):
    name = "adobomall"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        stockStatus = 'Unknown';
        title = response.css('div.pd_content div.pd_details.pd_title div.row div')
        title = title.css('div::text').extract()
        price = response.css('div.pd_price::text').extract()
        db.insertData(title, price, stockStatus, self.name)

