analURL = "http://vip.stock.finance.sina.com.cn/q/go.php/vIR_RatingNewest/index.phtml?p={}"

import tushare_wrapper as tuw
from pyquery import PyQuery as pq
import requests

resPyQuery = pq(requests.get(analURL.format(1)).content)

res = resPyQuery('tr')
print(len(res))
for i in range(1, len(res)):
    print(res("td").eq(13*i).text())


