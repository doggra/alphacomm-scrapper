""" Some utils functions """

import xlwt
import json
from b2bsoft.items import ShopItem
from HTMLParser import HTMLParser
from scrapy.utils.project import get_project_settings


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

def create_excel(spider):
        """ Create EXCEL """

        settings = get_project_settings()

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Scraped')

        # create header row
        for i, fieldname in enumerate(settings.get('FIELDS_TO_EXPORT')):

            if fieldname in ('sku', 'msrp', 'upc'):
                header = fieldname.upper()

            elif fieldname == "is_serial":
                header = "Is Serial"
            elif fieldname == "short_desc":
                header = "Short Description"
            elif fieldname == "long_desc": 
                header = "Long Description"
            else:
                header = fieldname.title()

            ws.write(0, i, header)

        # get rows from source CSV file
        with open("{}.csv".format(spider.name,)) as csv_file:

            # TODO: we want to skip all records that have empty 
            # fields except UPC, cost and MSRP (since we're populating 
            # these ourselves) for Excel extract

            line = 1

            # skip first line (header)
            next(csv_file)

            # fetch data from every row
            for row in csv_file:
                row_data_in_list = row.split("|")
                for i, cell in enumerate(row_data_in_list):
                    ws.write(line, i, cell)
                line += 1

        # save to EXCEL
        wb.save("{}.xls".format(spider.name,))
