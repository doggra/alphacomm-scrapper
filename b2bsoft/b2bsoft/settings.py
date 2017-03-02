# -*- coding: utf-8 -*-

BOT_NAME = 'b2bsoft'
SPIDER_MODULES = ['b2bsoft.spiders']
NEWSPIDER_MODULE = 'b2bsoft.spiders'

USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
ROBOTSTXT_OBEY = False

FEED_EXPORTERS = {
	'csv': 'b2bsoft.exporters.CsvExporter'
}

FIELDS_TO_EXPORT = [
	'vendor',
	'sku',
	'upc',
	'is_serial',
	'short_desc',
	'long_desc',
	'msrp',
	'cost',
	'department',
	'category',
	'manufacturer',
	'active',
]

CSV_DELIMITER = "|"

CONCURRENT_REQUESTS = 1
CONCURRENT_REQUESTS_PER_DOMAIN = CONCURRENT_REQUESTS
CONCURRENT_REQUESTS_PER_IP = CONCURRENT_REQUESTS

#COOKIES_ENABLED = False
#TELNETCONSOLE_ENABLED = False

#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

#SPIDER_MIDDLEWARES = {
#    'b2bsoft.middlewares.B2BsoftSpiderMiddleware': 543,
#}

#DOWNLOADER_MIDDLEWARES = {
#    'b2bsoft.middlewares.MyCustomDownloaderMiddleware': 543,
#}

#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# ITEM_PIPELINES = {'b2bsoft.pipelines.CSVPipeline': 300 }

# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False