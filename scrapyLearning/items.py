# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapylearningItem(scrapy.Item):
    # define the fields for your item here like:
    tag = scrapy.Field()
    imgUrl = scrapy.Field()
    pass
