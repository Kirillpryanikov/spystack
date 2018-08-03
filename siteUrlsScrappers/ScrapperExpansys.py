import scrapy


class ExpansysSpider(scrapy.Spider):
    name = "expansys"
    start_urls = [
        'http://www.expansys.ph/mobile-phones/',
    ]

    def parse(self, response):
        for elem in response.css('div.productGrid ul.item'):
            yield {
                'title': elem.css('li.title h3 a::text').extract_first(),
                'link': 'http://www.expansys.ph/' + elem.css('li.title h3 a::attr("href")').extract_first(),
            }
        next_page = response.css('li.pagination li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
