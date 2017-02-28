# -*- coding: utf-8 -*-
import scrapy
import json


class AlphacommSpider(scrapy.Spider):
    name = "alphacomm"
    allowed_domains = ["shopalphacomm.com"]
    start_urls = ['http://shopalphacomm.com/api/items?include=facets&fieldset=detail']

    def parse(self, response):
        """ Get all item groups """

        jsonresponse = json.loads(response.body_as_unicode())

        # Fetch "facets" dictionary
        facets = jsonresponse['facets']

        # Fetch items groups dictionary
        custitem_groupids_dict = facets[3]

        # Check if fetched correct dictionary and get all groups IDs
        if custitem_groupids_dict['id'] == "custitem_groupid":
            item_groups_ids = [ d['label'] for d in custitem_groupids_dict['values'] if 'label' in d ]

        print(item_groups_ids)