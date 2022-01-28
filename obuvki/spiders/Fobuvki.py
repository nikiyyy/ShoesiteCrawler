import scrapy
from obuvki.items import ObuvkiItem
from scrapy.loader import ItemLoader

class FobuvkiSpider(scrapy.Spider):
    name = 'Fobuvki'
    allowed_domains = ['www.districtshoes.bg']
    start_urls = ['https://www.districtshoes.bg/jeni-obuvki?orderBy=default&showBy=80&page=1']

    def parse(self, response):
        data = response.css('div.item.preview')

        for product in data:
            l = ItemLoader(item = ObuvkiItem(), selector=product)

            l.add_css('brand','a.item-brand::text')
            l.add_css('name','a.title::text')
            l.add_css('price','span.current::text')

            yield l.load_item()

        next_page
