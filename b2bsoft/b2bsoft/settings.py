# -*- coding: utf-8 -*-

BOT_NAME = 'b2bsoft'
SPIDER_MODULES = ['b2bsoft.spiders']
NEWSPIDER_MODULE = 'b2bsoft.spiders'

USER_AGENT = 'b2bsoft (+http://www.yourdomain.com)'
ROBOTSTXT_OBEY = False

#DOWNLOAD_DELAY = 3
#CONCURRENT_REQUESTS = 32
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

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

#ITEM_PIPELINES = {
#    'b2bsoft.pipelines.B2BsoftPipeline': 300,
#}


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


# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
