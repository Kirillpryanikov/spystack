import scrapy


class ShopeeSpider(scrapy.Spider):
    name = "shopee"
    start_urls = [
        'https://shopee.ph/Mobiles-cat.109.925?page=0&sortBy=pop',
    ]

    def parse(self, response):
        self.log('sad %s' % response.css('div.shopee-search-item-result div.shopee-search-item-result__item').extract_first())
        for index, elem in response.css('div.shopee-search-item-result div.shopee-search-item-result__item'):
            self.log('zzz %d' % index)
            yield {
                'title': elem.css('a.shopee-item-card--link::text').extract_first(),
                'link': elem.css('a.shopee-item-card--link::attr("href")').extract_first(),
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
