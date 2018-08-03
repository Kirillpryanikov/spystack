import scrapy


class SavenearnSpider(scrapy.Spider):
    name = "savenearn"
    start_urls = [
        'https://savenearn.com.ph/product-category/mobile-gadgets/smartphones/page/11/',
    ]

    def parse(self, response):
        for elem in response.css('div.products-layout div.product'):
            yield {
                'title': elem.css('div.caption h3.name a::text').extract_first(),
                'link': elem.css('div.caption h3.name a::attr("href")').extract_first()
            }
        next_pages = response.css('a.page-numbers::attr("href")')
        for page, pageCur in next_pages:
            if page.xpath('@class').extract().find('current'):
                next_page = pageCur
        # next_page = response.css('a.page-numbers::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)

