Alphacomm WebScraper
====================
This is shopalphacomm.com scraper for obtaining products from shop catalog.


Project installation
--------------------

{code}
$ sudo apt-get install python-dev python-pip libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev virtualenv
{code}

>>> $ virtualenv env
>>> $ source env/bin/activate
>>> $ pip install -U pip
>>> $ pip install -r requirements.txt


Running spider
--------------
>>> $ cd ./b2bsoft
>>> $ scrapy crawl alphacomm


Settings
--------
All settings are located in b2bsoft/b2bsoft/settings.py . 
These below are the most important ones.
More on docs: https://doc.scrapy.org/en/latest/topics/settings.html

* FEED_URI `output file for scraping data`
* FIELDS_TO_EXPORT `list of fields for export. If you add new field into ShopItem (items.py), you also need to add it here. This option must be specified to set specific order of fields in export file
* CSV_DELIMITER `delimiter for CSV file`
* CONCURRENT_REQUESTS `max number of concurrent connections to scraped site (dont set too high because it can DoS their server)`
* LOG_FILE `filename for scraper log`
* LOG_LEVEL `level of scraper logger`


Command line parameters
-----------------------
You can add these to your command line if running spider from shell:

* -L LEVEL `debug level (ERROR, WARNING, INFO)`
* -o filename.csv `scrap items to filename.csv`
* --logfile=name.log `specify log filename as 'name.log'`