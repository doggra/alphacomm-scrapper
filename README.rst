Project installation
--------------------

>>> $ virtualenv env
>>> $ source env/bin/activate
>>> $ pip install -r requirements.txt


Running spider
--------------

>>> scrapy crawl -o alphacomm_`date +%s`.csv alphacomm -L INFO --logfile=./alphacomm.log


Logging
-------

All loging goes to `alphacomm.log`