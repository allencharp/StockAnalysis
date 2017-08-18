First, get the data from sina http://vip.stock.finance.sina.com.cn/q/go.php/vIR_RatingNewest/index.phtml

save the stock into mysql

Second, analysis the data with tushare, to see which analysist's forcast get the most profitable stock

Third, use weixin public account, setup a simple webservice to interactive with users

------------------------------

sina_read.py python web crawler for sina data

crontab -e

* * * * * python3 sina_read.py 

sina_service.py  flask weixin service

sudo python3 sina_service.py 

requesities:

python3

mysql

tushare

pyquery

flask

gevent
