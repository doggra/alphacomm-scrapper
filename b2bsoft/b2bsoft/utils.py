""" Some utils functions """

import json
from b2bsoft.items import ShopItem
from HTMLParser import HTMLParser

def create_new_item():
    it = ShopItem()
    it['vendor'] = "Alphacomm"
    it['is_serial'] = 0
    it['cost'] = 0
    it['msrp'] = 0
    it['department'] = "Accessory"
    it['active'] = 1
    return it

def get_json_from_response(response):
    """ Get json from API response """
    return json.loads(response.body_as_unicode())

def close_spider(message=""):
    """ Close spider with msg to logger """
    raise CloseSpider(reason=message)