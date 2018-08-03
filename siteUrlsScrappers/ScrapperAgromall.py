import scrapy


class ArgomallSpider(scrapy.Spider):
    name = "argomall"
    start_urls = [
        'https://www.argomall.com/smartphones',
    ]

    def parse(self, response):
        for elem in response.css('div.category-products li.item'):
            yield {
                'title': elem.css('div.product-content-wrapper h3.product-name a::text').extract_first(),
                'link': elem.css('div.product-content-wrapper h3.product-name a::attr("href")').extract_first(),
            }
        next_page = response.css('div.pages a.next::attr("href")').extract_first()

        if next_page is not None:
            yield response.follow(next_page, self.parse)
