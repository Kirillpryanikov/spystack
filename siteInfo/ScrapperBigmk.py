import scrapy
from DatabaseConnection import DataBaseConnection


class BigmkSpider(scrapy.Spider):
    name = "bigmk"

    def parse(self, response):
        db = DataBaseConnection();
        if response.status == 404:
            db.insertErrorLink(response.url)
            return

        if response.css('div.summary p.pempty').extract_first() is not None:
            stockStatus = 'Out of Stock';
        else:
            stockStatus = 'In Stock';

        priceScript = response.xpath('//script[contains(text(), "sell_price")]/text()').extract();
        price = None;
        if priceScript != []:
            priceStartIndex = priceScript[len(priceScript) - 1].find("sell_price") + 13;
            priceEndIndex = priceScript[len(priceScript) - 1].find('"', priceStartIndex);
            price = priceScript[len(priceScript) - 1][priceStartIndex:priceEndIndex]
        title = response.css('div.summary h2::text').extract_first();
        db.insertData(title, price, stockStatus, self.name)
