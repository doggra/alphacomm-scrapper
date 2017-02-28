# -*- coding: utf-8 -*-

__author__ = "Radosław (Doggra) Przytuła"
__email__ = "doggra@protonmail.com"

import scrapy
import json
from scrapy.exceptions import CloseSpider
from b2bsoft.items import ShopItem

def get_json_from_response(response):
    """ Get json from API response """
    return json.loads(response.body_as_unicode())

def close_spider(message=""):
    """ Close spider with msg to logger """
    raise CloseSpider(reason=message)


class AlphacommSpider(scrapy.Spider):
    """ Shopalphacomm.com spider """

    name = "alphacomm"
    allowed_domains = ["shopalphacomm.com"]
    start_urls = ['http://shopalphacomm.com/api/items?include=facets'\
                                                  +'&fieldset=detail']

    def __init__(self):
        self.scrapped_sku = []

    def parse(self, response):
        """ Initial crawling function. Get all item groups 
        """

        jsonresponse = get_json_from_response(response)

        # Find dicitionary containing customitem groups and make a list of it
        try:
            custitem_groupid = next((d for d in jsonresponse['facets']\
                              if d['id'] == "custitem_groupid"), None)
        except KeyError:
            close_spider('No `facets` dict found')

        item_groups_ids = [ d['label'] for d in custitem_groupid['values']\
                                                         if 'label' in d ]

        # Generate requests for item groups
        for group_id in item_groups_ids[:2]:
            yield scrapy.Request(

                "http://shopalphacomm.com/api/items?include=facets&"\
                    +"custitem_groupid={}&fieldset=details".format(group_id,),

                callback=self.item_group_details,
                meta={'groupid': group_id}
            )

    def item_group_details(self, response):
        """ Get specific item group details 
        """

        item = ShopItem()
        jsonresponse = get_json_from_response(response)

        # Get list of group items
        items_list = jsonresponse['items']

        brand_dict = next((d for d in jsonresponse['facets'] \
                  if d['id'] == "custitem_sca_brand"), None)

        brands_list = ' '.join([ b['label'] for b in brand_dict['values'] ])

        item['manufacturer'] = brands_list

        yield item