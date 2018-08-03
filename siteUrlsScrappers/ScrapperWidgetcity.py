import scrapy


class WidgetcitySpider(scrapy.Spider):
    name = "widgetcity"
    start_urls = [
        'http://www.widgetcity.com.ph/mobile',
    ]

    def parse(self, response):
        for elem in response.css('div.product-layout'):
            yield {
                'title': elem.css('div.product-inner h2.product-name a::text').extract_first().strip(),
                'link': elem.css('div.product-inner h2.product-name a::attr("href")').extract_first(),
            }
        next_page = response.css('li.pages-item-next a.next::attr("href")').extract_first()

        if next_page is not None:
            yield response.follow(next_page, self.parse)
