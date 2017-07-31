analURL = "http://vip.stock.finance.sina.com.cn/q/go.php/vIR_RatingNewest/index.phtml"

import tushare_wrapper as tuw
from pyquery import PyQuery as pq
import pymysql


conn = pymysql.connect(host="127.0.0.1",  user='root', password='355585', db='allen')

respyquery = pq(url=analURL)
stock = respyquery('tr')

for i in range(1, len(stock)):
    print(stock("td").eq(13*i).text())


cur = conn.cursor()
cur.execute("SELECT * FROM city")
for r in cur:
    print(r)
cur.close()
conn.close()