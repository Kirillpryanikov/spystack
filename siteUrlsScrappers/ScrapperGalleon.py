import scrapy


class GalleonSpider(scrapy.Spider):
    name = "galleon"
    start_urls = [
        'https://www.galleon.ph/category/3278/unlocked-cell-phones?page=1',
    ]

    def parse(self, response):
        for elem in response.css('div.product-vertical-list div.product'):
            yield {
                'title': elem.css('div.product-name a::text').extract_first(),
                'link': 'https://www.galleon.ph' + elem.css('div.product-name a::attr("href")').extract_first(),
            }
        next_page = response.css('div.pages a.next::attr("href")').extract_first()

        if next_page is not None:
            yield response.follow(next_page, self.parse)
