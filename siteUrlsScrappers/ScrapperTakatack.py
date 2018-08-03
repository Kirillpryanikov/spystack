import scrapy


class TakatackSpider(scrapy.Spider):
    name = "takatack"
    start_urls = [
        'https://www.takatack.com/category/electronics',
    ]

    def parse(self, response):
        for elem in response.css('div.list div.item'):
            yield {
                'title': elem.css('div.text a.product-title::text').extract_first().strip(),
                'link': 'https://www.takatack.com' + elem.css('div.text a.product-title::attr("href")').extract_first(),
            }
        next_page = 'https://www.takatack.com' + response.css('a[id="load-more"]::attr("href")').extract_first()

        if next_page is not None:
            yield response.follow(next_page, self.parse)
