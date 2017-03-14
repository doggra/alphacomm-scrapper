# -*- coding: utf-8 -*-

from scrapy import Item, Field

class ShopItem(Item):
    vendor = Field()
    sku = Field()
    upc = Field()
    is_serial = Field()
    short_desc = Field()
    long_desc = Field()
    msrp = Field()
    cost = Field()
    department = Field()
    category = Field()
    manufacturer = Field()
    active = Field()
    brochure = Field()
    video = Field()
    image_urls = Field()
    image_paths = Field()
    scrap_link = Field()

