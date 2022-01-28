from gc import callbacks
import scrapy
from obuvki.items import ObuvkiItem
from scrapy.loader import ItemLoader

class FobuvkiSpider(scrapy.Spider):
    name = 'Fobuvki'
    allowed_domains = ['www.districtshoes.bg']
    start_urls = ['https://www.districtshoes.bg/jeni-obuvki?page=1&orderBy=default&showBy=80']

    def parse(self, response):
        data = response.css('div.item.preview')

        for product in data:
            l = ItemLoader(item = ObuvkiItem(), selector=product)

            l.add_css('brand','a.item-brand::text')
            l.add_css('name','a.title::text')
            l.add_css('price','span.current::text')

            yield l.load_item()

        next_page = response.css('ul.pagination.list-unstyled').css('a::attr(href)').getall()[-1]
        #print("https://www.districtshoes.bg" + next_page)
        #print(response.request.url)
        #print(type(next_page))
        #print(type(response.request.url))
        if next_page is not None and response.request.url != "https://www.districtshoes.bg" + next_page:
            yield response.follow(next_page, callback = self.parse)
        
