Project installation
--------------------

>>> $ virtualenv env
>>> $ source env/bin/activate
>>> $ pip install -r requirements.txt


Running spider
--------------

>>> $ scrapy crawl -L INFO \
                   -o alphacomm_`date +%s`.csv \
                   --logfile=./alphacomm.log alphacomm



Command line parameters
-----------------------

* -L LEVEL `debug level (ERROR, WARNING, INFO)`
* -o filename.csv `scrap items to filename.csv`
* --logfile=name.log `specify log filename as 'name.log'`