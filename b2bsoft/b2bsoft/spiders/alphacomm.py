# -*- coding: utf-8 -*-

__author__ = "Radosław (Doggra) Przytuła"
__email__ = "doggra@protonmail.com"

import scrapy
from scrapy.exceptions import CloseSpider
from b2bsoft.utils import get_json_from_response, close_spider, create_new_item, strip_tags


class AlphacommSpider(scrapy.Spider):
    """ Shopalphacomm.com spider 
        API URL: http://shopalphacomm.com/api/items 
    """

    name = "alphacomm"
    allowed_domains = ["shopalphacomm.com"]
    start_urls = ['http://shopalphacomm.com/api/items?include=facets'\
                                                  +'&fieldset=detail']

    def __init__(self):
        self.scrapped_sku = []

    def parse(self, response):
        """ Initial crawling function. 
        """

        jsonresponse = get_json_from_response(response)

        # find dicitionary containing customitem groups
        try:
            custitem_groupid = next((d for d in jsonresponse['facets']\
                              if d['id'] == "custitem_groupid"), None)
        except KeyError:
            close_spider('No `facets` dict found')

        # create list of groupids
        item_groups_ids = [ d['label'] for d in custitem_groupid['values']\
                                                         if 'label' in d ]
        # make request for every groupid
        for group_id in item_groups_ids:

            yield scrapy.Request(

                "http://shopalphacomm.com/api/items?include=facets&"\
                    +"custitem_groupid={}&fieldset=details".format(group_id,),

                callback=self.item_group_details,
                meta={'groupid': group_id}
            )

    def item_group_details(self, response):
        """ Get specific item group details """

        # Get all items from group
        jsonresponse = get_json_from_response(response)
        items_list = jsonresponse['items']

        # Export each item
        for item in items_list:

            it = create_new_item()

            # get producttype and brand from response
            cat = next((d for d in jsonresponse['facets'] \
                      if d['id'] == "custitem_sca_producttype"), None)
            brand_dict = next((d for d in jsonresponse['facets'] \
                      if d['id'] == "custitem_sca_brand"), None)
            brands = ', '.join([ b['label'] for b in brand_dict['values'] ])

            # populate item fields
            it['long_desc'] = item['storedetaileddescription'].replace('\r\n', ' ').strip("\"")
            it['category'] = cat['values'][0]['label']
            it['manufacturer'] = brands
            it['sku'] = item['itemid']
            it['upc'] = item['custitem_upc']
            it['short_desc'] = item['storedescription']

            # log event: no price set
            try:
                it['cost'] = "${}".format(item['onlinecustomerprice'],)

            except KeyError, e:
                self.logging.error(str(e))

            # done, save item
            self.scrapped_sku.append(item['itemid'])
            yield it
