import scrapy


class LazadaSpider(scrapy.Spider):
    name = "lazada"
    start_urls = [
        'https://www.lazada.com.ph/shop-mobiles/?page=1',
    ]

    def parse(self, response):
        self.log('sad %s' % response.xpath('//script[@type="application/ld+json"]').extract_first())
        for index, elem in response.xpath('//div[@data-qa-locator="product-item"]'):
            self.log('zzz %d' % index)
            yield {
                'title': elem.css('div.shopee-item-card--link::text').extract_first(),
                'link': elem.css('div.shopee-item-card--link::attr("href")').extract_first(),
            }
        next_pages = response.css('a.page-numbers')
        next_page = None
        self.log('aaaa %s' % next_pages)
        for count, page in enumerate(next_pages):
            self.log('qwer %s %s' % page, page.xpath('a/class()').extract_first())
            if page.xpath('a/class()').extract_first().find('current'):
                next_page = page[count + 1].css('a::attr("href")').extract_first()
                self.log('xxx %s' % next_page)
        # for page, pageCur in next_pages:
        #     if page.xpath('@class').extract().find('current'):
        #         next_page = pageCur
        # next_page = response.css('a.page-numbers::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
