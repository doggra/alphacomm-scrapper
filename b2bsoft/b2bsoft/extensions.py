""" Extension for generating EXCEL file """

import xlwt
from scrapy import signals
from scrapy.utils.project import get_project_settings

def create_excel(spider):
        """ Create EXCEL """

        settings = get_project_settings()

        csv_filename = settings.get('FEED_URI', 'test.csv')

        wb = xlwt.Workbook(encoding='utf-8')
        ws = wb.add_sheet('Scraped')

        # create header row
        for i, fieldname in enumerate(settings.get('FIELDS_TO_EXPORT')):

            if fieldname in ('sku', 'msrp', 'upc'):
                header = fieldname.upper()

            elif fieldname == "is_serial":
                header = "Is serial"
            elif fieldname == "short_desc":
                header = "Short Description"
            elif fieldname == "long_desc":
                header = "Long Description"
            else:
                header = fieldname.title()

            ws.write(0, i, header)

        # get rows from source CSV file
        with open(csv_filename) as csv_file:

            # skip first line (header)
            next(csv_file)
            line = 1

            # fetch data from every line
            for row in csv_file:

                # get row data
                row_data = row.split("|")

                # required fields - skip if any doesn't exist
                required_fields = [
                    row_data[0],
                    row_data[1],
                    row_data[3],
                    row_data[4],
                    row_data[5],
                    row_data[8],
                    row_data[9],
                    row_data[10],
                ]
                if '' in required_fields or None in required_fields:
                    continue

                # set max characters limits and write columns
                enumerated_row_data = enumerate(row_data)

                for i, cell in enumerated_row_data:

                    if i == 2:
                        cell = cell[:50]

                    elif i == 4:
                        cell = cell[:255]

                    elif i == 5:
                        cell = cell[:1000]

                    elif i == 9:
                        cell = cell[:20]

                    elif i == 10:
                        cell = cell[:50]

                    ws.write(line, i, cell)

                line += 1

        # create EXCEL file
        wb.save(csv_filename.replace('csv', 'xls'))

class ExcelExtension(object):

    @classmethod
    def from_crawler(cls, crawler):
        ext = cls()
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        return ext

    def spider_closed(self, spider):
        spider.logger.info('Generating EXCEL file')
        create_excel(spider)