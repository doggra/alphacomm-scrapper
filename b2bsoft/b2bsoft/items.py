# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShopItem(scrapy.Item):
	vendor = scrapy.Field()
    manufacturer = scrapy.Field()
    msrp = scrapy.Field()
    pass
