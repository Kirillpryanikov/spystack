import scrapy


class BigmkSpider(scrapy.Spider):
    name = "bigmk"
    start_urls = [
        'https://www.bigmk.ph/c-mobiles-tablets-563.html',
    ]

    def parse(self, response):
        for elem in response.css('li.items-gallery.itemsList'):
            yield {
                'title': elem.css('div.goodinfo h3 a.entry-title::text').extract_first().strip(),
                'link': 'https://www.bigmk.ph' + elem.css('div.goodinfo h3 a.entry-title::attr("href")').extract_first(),
            }
        next_page = response.css('div.pages_bar a::attr("href")').extract()[-2]

        if next_page is not None:
            yield response.follow(next_page, self.parse)
