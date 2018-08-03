import scrapy


class BigbentaSpider(scrapy.Spider):
    name = "bigbenta"
    start_urls = [
        'https://bigbenta.com/store-category/consumer-electronic',
    ]

    def parse(self, response):
        for elem in response.css('div.product-box'):
            yield {
                'title': elem.css('div.product-desc a.product-name::text').extract_first(),
                'link': elem.css('div.product-desc a.product-name::attr("href")').extract_first(),
            }
        next_page = response.css('ul.pagination a.page-link::attr("href")').extract()[-1]
        if next_page is not None:
            yield response.follow(next_page, self.parse)
