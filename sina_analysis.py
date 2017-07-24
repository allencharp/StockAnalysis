analURL = "http://vip.stock.finance.sina.com.cn/q/go.php/vReport_List/kind/company/index.phtml?p={}"

import tushare_wrapper as tuw
from pyquery import PyQuery as pq
import requests

resPyQuery = pq(requests.get(analURL.format(1)).content)

print(resPyQuery)


