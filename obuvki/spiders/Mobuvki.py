import scrapy


class MobuvkiSpider(scrapy.Spider):
    name = 'Mobuvki'
    allowed_domains = ['www.districtshoes.bg']
    start_urls = ['https://www.districtshoes.bg/muje-obuvki?orderBy=default&showBy=80&page=1']

    def parse(self, response):
        data = response.css('div.item.preview')

        for product in data:
            yield {
                'brand' : product.css('a.item-brand::text').get()[1:] ,
                'name' : product.css('a.title::text').get()[8:-1] ,
                'price' : product.css('span.current::text').get()[:-5]
            }

