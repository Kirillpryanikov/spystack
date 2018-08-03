import scrapy


class OtcerSpider(scrapy.Spider):
    name = "otcer"
    start_urls = [
        'https://www.otcer.ph/product-category/mobile-phones/',
    ]

    def parse(self, response):
        for elem in response.css('ul.products li.product'):
            yield {
                'title': elem.css('div.product-inner a h2::text').extract_first(),
                'link': elem.css('div.product-inner a::attr("href")').extract_first(),
            }
        next_page = response.css('div.pages a.next::attr("href")').extract_first()

        if next_page is not None:
            yield response.follow(next_page, self.parse)
