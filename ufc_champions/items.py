# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class UfcChampionsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    flyweight = scrapy.Field()
    bantamweight = scrapy.Field()
    featherweight = scrapy.Field()
    lightweight = scrapy.Field()
    welterweight = scrapy.Field()
    middleweight = scrapy.Field()
    lightheavyweight = scrapy.Field()
    heavyweight = scrapy.Field()
    wstrawweight = scrapy.Field()
    wbantamweight = scrapy.Field()
    wfeatherweight = scrapy.Field()
    name = scrapy.Field()
    record = scrapy.Field()
    pass
