# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst, MapCompose

def process_brand(value):
    return value[1:]

def process_name(value):
    return value[8:-1] 

def process_price(value):
    return value[:-5]

class ObuvkiItem(scrapy.Item):
    brand = scrapy.Field(input_processor = MapCompose(process_brand), output_processor = TakeFirst())
    name = scrapy.Field(input_processor = MapCompose(process_name), output_processor = TakeFirst())
    price = scrapy.Field(input_processor = MapCompose(process_price), output_processor = TakeFirst())
