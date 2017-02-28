# -*- coding: utf-8 -*-

from scrapy import signals

class B2BsoftPipeline(object):
    def process_item(self, item, spider):
        return item
