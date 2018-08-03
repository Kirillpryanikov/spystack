import scrapy


class AdobomallSpider(scrapy.Spider):
    name = "adobomall"
    start_urls = [
        'https://www.abenson.com/mobile/smartphone.html',
    ]

    def parse(self, response):
        for elem in response.css('ol.products li.product'):
            yield {
                'title': elem.css('h4.product-item-name::text').extract_first(),
                'link': elem.css('h4.product-item-name a.product-item-link::attr("href")').extract_first(),
            }
        next_page = response.css('li.pages-item-next a.next::attr("href")').extract_first()

        if next_page is not None:
            yield response.follow(next_page, self.parse)
