import scrapy


class MemoxpressSpider(scrapy.Spider):
    name = "memoxpress"
    start_urls = [
        'http://store.memoxpress.ph/index.php?rt=product/category&path=71',
    ]

    def parse(self, response):
        for elem in response.css('div.grid.list-inline div.fixed_wrapper'):
            yield {
                'title': elem.css('a.prdocutname::text').extract_first(),
                'link': elem.css('a.prdocutname::attr("href")').extract_first(),
            }
        next_page = response.css('ul.pagination a::attr("href")').extract()[-2]
        if next_page is not None:
            yield response.follow(next_page, self.parse)
