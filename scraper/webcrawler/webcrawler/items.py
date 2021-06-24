# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WebcrawlerItem(scrapy.Item):
    url=scrapy.Field()
    property_type = scrapy.Field()
    location = scrapy.Field()
    block = scrapy.Field()
    distance_from_center = scrapy.Field()
    add_type = scrapy.Field()
    size = scrapy.Field()
    year = scrapy.Field()
    area = scrapy.Field()
    storey = scrapy.Field()
    total_storeys = scrapy.Field()
    registered = scrapy.Field()
    heat_type = scrapy.Field()
    rooms = scrapy.Field()
    toiletes = scrapy.Field()
    parking = scrapy.Field()
    price = scrapy.Field()
    other = scrapy.Field()
