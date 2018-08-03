import scrapy


class PounditSpider(scrapy.Spider):
    name = "poundit"
    start_urls = [
        'https://www.poundit.com/pages/smartphones',
    ]

    def parse(self, response):
        for elem in response.css('div.homepage-product-slider div.product-wrap'):
            yield {
                'title': elem.css('a.product-info__caption span.title::text').extract_first().strip(),
                'link': 'https://www.poundit.com' + elem.css('a.product-info__caption::attr("href")').extract_first(),
            }
