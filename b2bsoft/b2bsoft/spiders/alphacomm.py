# -*- coding: utf-8 -*-

__author__ = "Radosław (Doggra) Przytuła"
__email__ = "doggra@protonmail.com"

import scrapy
from scrapy.exceptions import CloseSpider
from b2bsoft.utils import get_json_from_response, close_spider, create_new_item

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

        try:
            # to find dicitionary containing items groups (facets/custitem_groupid)
            custitem_groupid = next((d for d in jsonresponse['facets']\
                              if d['id'] == "custitem_groupid"), None)
        except KeyError:
            close_spider('No `facets` dict found')

        # prepare list of groupids
        item_groups_ids = [ d['label'] for d in custitem_groupid['values']\
                                                         if 'label' in d ]
        # make request for every group
        for group_id in item_groups_ids[:1]:

            yield scrapy.Request(
                self.get_group_url(group_id),
                callback=self.item_group_details,
                meta={
                    'groupid': group_id
                }
            )

    def item_group_details(self, response):
        """ Item group details """

        self.logger.info("SCRAPED: {}".format(response.request.url,))
        # get all items from that group
        jsonresponse = get_json_from_response(response)
        items_list = jsonresponse['items']

        # export each item
        for item in items_list:

            it = create_new_item()

            # find objects by `id` key
            cat = next((d for d in jsonresponse['facets'] \
                      if d['id'] == "custitem_sca_producttype"), None)
            bra = next((d for d in jsonresponse['facets'] \
                      if d['id'] == "custitem_sca_brand"), None)
            brands = ', '.join([ b['label'] for b in bra['values'] ])

            # populate fields
            it['category'] = cat['values'][0]['label']
            it['manufacturer'] = brands
            it['sku'] = item['itemid']
            it['upc'] = item['custitem_upc']
            it['short_desc'] = item['storedescription']

            # clean long description field
            desc = item['storedetaileddescription']
            it['long_desc'] = ' '.join(desc.split()).replace("\"\"", "\"")

            # # log event: no price set
            # try:
            #     it['cost'] = "${}".format(item['onlinecustomerprice'],)

            # except KeyError, e:
            #     self.logger.warning(str(e))

            # done, save item
            self.scrapped_sku.append(item['itemid'])
            yield it


    def get_group_url(self, group_id):
        """ Prepare url for group details 
        """
        url = "http://shopalphacomm.com/api/items?custitem_groupid={}".format(group_id,)
        url += "&include=facets&fieldset=details"
        return url