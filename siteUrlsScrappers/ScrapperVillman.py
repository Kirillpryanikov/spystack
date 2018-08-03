import scrapy


class VillmanSpider(scrapy.Spider):
    name = "villman"
    start_urls = [
        'http://villman.com/Category/Smart-Phones/90/',
    ]

    def parse(self, response):
        for elem in response.css('div[id="category_list"] table'):
            yield {
                'title': elem.css('span.prodname a::text').extract_first().strip(),
                'link': 'http://villman.com' + elem.css('span.prodname a::attr("href")').extract_first(),
            }
        next_page = response.css('li.pages-item-next a.next::attr("href")').extract_first()

        if next_page is not None:
            yield response.follow(next_page, self.parse)
