import scrapy


class GoodsSpider(scrapy.Spider):
    name = "goods"
    start_urls = [
        'https://www.goods.ph/category/online-shopping-mobiles-and-tablets-159.html',
    ]

    def parse(self, response):
        for elem in response.css('div.product-list div.item'):
            yield {
                'title': elem.css('div.product-head a::text').extract_first().strip(),
                'link': 'https://www.goods.ph' + elem.css('div.product-head a::attr("href")').extract_first(),
            }
        next_page = response.css('div.product-bottom a::attr("href")').extract()[-1]

        if next_page is not None:
            yield response.follow(next_page, self.parse)
