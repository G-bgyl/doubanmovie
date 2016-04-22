# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanmovieItem(scrapy.Item):
    title = scrapy.Field()
    director = scrapy.Field()
    screenwriter = scrapy.Field()
    actor = scrapy.Field()
    type = scrapy.Field()
    mov_date = scrapy.Field()
    mov_country = scrapy.Field()
    mov_language = scrapy.Field()
    mov_length = scrapy.Field()
    mov_introducton = scrapy.Field()
    pass

