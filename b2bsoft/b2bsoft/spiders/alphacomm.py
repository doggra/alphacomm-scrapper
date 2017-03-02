# -*- coding: utf-8 -*-
import scrapy


class AlphacommSpider(scrapy.Spider):
    name = "alphacomm"
    allowed_domains = ["shopalphacomm.com"]
    start_urls = ['http://shopalphacomm.com/']

    def parse(self, response):
        pass
