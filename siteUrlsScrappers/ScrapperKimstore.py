import scrapy


class KimstoreSpider(scrapy.Spider):
    name = "kimstore"
    start_urls = [
        'https://kimstore.com/mobile-phones.html',
    ]

    def parse(self, response):
        for elem in response.css('ol.products li.product'):
            yield {
                'title': elem.css('div.product-item-details h2.product-item-name a.product-item-link::text').extract_first().strip(),
                'link': elem.css('div.product-item-details h2.product-item-name a.product-item-link::attr("href")').extract_first(),
            }
        next_page = response.css('li.pages-item-next a.next::attr("href")').extract_first()

        if next_page is not None:
            yield response.follow(next_page, self.parse)
