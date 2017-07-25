analURL = "http://vip.stock.finance.sina.com.cn/q/go.php/vIR_RatingNewest/index.phtml"

import tushare_wrapper as tuw
from pyquery import PyQuery as pq


respyquery = pq(url=analURL)
stock = respyquery('tr')

for i in range(1, len(stock)):
    print(stock("td").eq(13*i).text())


