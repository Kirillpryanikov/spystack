import scrapy


class ElnstoreSpider(scrapy.Spider):
    name = "elnstore"
    start_urls = [
        'http://www.elnstore.com/smartphones.html/?limit=36',
    ]

    def parse(self, response):
        for elem in response.css('ul.products-grid li.item'):
            yield {
                'title': elem.css('div.product-shop h2.product-name a::text').extract_first().strip(),
                'link': elem.css('div.product-shop h2.product-name a::attr("href")').extract_first(),
            }
