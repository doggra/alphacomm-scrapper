""" Some helper functions """

import json

def get_json_from_response(response):
    """ Get json from API response """
    return json.loads(response.body_as_unicode())

def close_spider(message=""):
    """ Close spider with msg to logger """
    raise CloseSpider(reason=message)
