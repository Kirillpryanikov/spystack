import scrapy


class AsianicSpider(scrapy.Spider):
    name = "asianic"
    start_urls = [
        'http://asianic.com.ph/product_list/smart-phonesphablets',
    ]

    def parse(self, response):
        for elem in response.css('div.prod_container'):
            yield {
                'title': elem.css('a.prodname::text').extract_first().strip(),
                'link': 'http://asianic.com.ph' + elem.css('a.prodname::attr("href")').extract_first(),
            }
