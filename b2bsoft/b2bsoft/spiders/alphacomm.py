# -*- coding: utf-8 -*-

""" Shopalphacomm scraper 
    API URL: http://shopalphacomm.com/api/items 
"""

__author__ = "Radosław (Doggra) Przytuła"
__email__ = "doggra@protonmail.com"
__version__ = "1.0.1"

import scrapy
from scrapy.exceptions import CloseSpider
from b2bsoft.utils import get_json_from_response, close_spider, create_new_item
from scrapy.utils.project import get_project_settings
from scrapy.selector import Selector

class AlphacommSpider(scrapy.Spider):

    name = "alphacomm"
    allowed_domains = ["shopalphacomm.com"]
    start_urls = ['http://shopalphacomm.com/api/items?include=facets'\
                                                  +'&fieldset=detail']

    def __init__(self):
        self.csv_delimiter = get_project_settings().get('CSV_DELIMITER', '')
        self.scrapped_sku = []


    def parse(self, response):
        """ Initial crawling function. """

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
        for group_id in item_groups_ids:

            yield scrapy.Request(
                self.get_group_url(group_id),
                callback=self.item_group_details,
                meta={
                    'groupid': group_id
                }
            )

    def item_group_details(self, response):
        """ Item group details """

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
            it['category'] = cat['values'][0]['label'][:20]
            it['manufacturer'] = brands[:50]
            it['sku'] = item['itemid']
            it['upc'] = item['custitem_upc'][:50]
            it['short_desc'] = item['pagetitle'].replace(self.csv_delimiter, " ")[:255]

            # clean long description field
            desc = item['storedetaileddescription']
            it['long_desc'] = ' '.join(desc.split()) \
                                 .replace("\"\"", "\"") \
                                 .replace("\r","") \
                                 .replace("\n","") \
                                 .replace(self.csv_delimiter, " ") \
                                 [:1000]

            extra_buttons_selector = Selector(
                text=item['custitem_sc_itemdetails_buttons']
            )

            video_link = extra_buttons_selector.css('iframe::attr(src)').extract()
            it['video'] = video_link

            all_extra_links = extra_buttons_selector.css('a')
            try:
                it['brochure'] = [ l.css('::attr(href)').extract()[0] for l in all_extra_links if l.css('::text').extract()[0] == "Download Brochure"][0]

                # relative link? add domain
                if it['brochure'].startswith("/"):
                    it['brochure'] = "http://shopalphacomm.com"+it['brochure']

            except IndexError:
                # item have no brochure
                it['brochure'] = ''

            # get images urls
            try:
                it['images'] = ', '.join([ u['url'] for u in item['itemimages_detail']['media']['urls'] ])
            except KeyError:
                # no images?
                it['images'] = ''

            it['scrap_link'] = response.request.url

            # UNCOMMENT FOR FETCHING ITEM PRICE
            # try:
            #     it['cost'] = "${}".format(item['onlinecustomerprice'],)
            # except KeyError, e:
            #     self.logger.warning(str(e))

            # done, save item
            self.scrapped_sku.append(item['itemid'])
            
            yield it

    def get_group_url(self, group_id):
        """ Prepare url for group details """

        url = "http://shopalphacomm.com/api/items?custitem_groupid={}".format(group_id,)
        url += "&include=facets&fieldset=details"
        return url