""" Some helper functions """

import json
from b2bsoft.items import ShopItem

def create_new_item():
	item = ShopItem()
	item['Vendor'] = "Alphacomm"
	return item

def get_json_from_response(response):
    """ Get json from API response """
    return json.loads(response.body_as_unicode())

def close_spider(message=""):
    """ Close spider with msg to logger """
    raise CloseSpider(reason=message)
