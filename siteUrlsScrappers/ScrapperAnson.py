import scrapy


class AnsonSpider(scrapy.Spider):
    name = "anson"
    start_urls = [
        'https://ansons.ph/product-category/smartphones/',
    ]

    def parse(self, response):
        for elem in response.css('ul.products li.product'):
            yield {
                'title': elem.css('div.product-meta-wrapper h3.product-title a::text').extract_first().strip(),
                'link': elem.css('div.product-meta-wrapper h3.product-title a::attr("href")').extract_first(),
            }
        next_page = response.css('li.pages-item-next a.next::attr("href")').extract_first()

        if next_page is not None:
            yield response.follow(next_page, self.parse)
