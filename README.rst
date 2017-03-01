Project installation
--------------------

>>> $ virtualenv env
>>> $ source env/bin/activate
>>> $ pip install -r requirements.txt


Running spider
--------------

>>> scrapy crawl \
                 -o alphacomm_`date +%s`.csv \
                 --logfile=./alphacomm.log alphacomm
                 -L INFO


Command line parameters
-----------------------
* -o filename.csv `scrap items to filename.csv`
* --logfile=name.log `specify log filename as 'name.log'`
* -L LEVEL `debug level (ERROR, WARNING, INFO)`