analURL = "http://vip.stock.finance.sina.com.cn/q/go.php/vReport_List/kind/company/index.phtml"

import tushare_wrapper as tuw
import pyquery as py
#import


result = tuw.get_stock_rate('601988','2017/01/01',30)

print(result)