# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class item(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()

class TutorialItem(scrapy.Item):
    item = {}
    url_nxt = scrapy.Field()