from scrapy import signals
from b2bsoft.utils import create_excel

class ExcelExtension(object):

    @classmethod
    def from_crawler(cls, crawler):
        ext = cls()
        crawler.signals.connect(ext.spider_closed, signal=signals.spider_closed)
        return ext

    def spider_closed(self, spider):
        spider.logger.info('Generating EXCEL file')
        create_excel(spider)