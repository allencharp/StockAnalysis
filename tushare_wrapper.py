import tushare as ts
from dateutil import parser
import datetime
#analURL = "http://vip.stock.finance.sina.com.cn/q/go.php/vReport_List/kind/company/index.phtml"

def get_stock_rate(s_code, s_start, period):
    stock = ts.get_h_data(code=s_code, autype="hfq", start=s_start,
                          end=str(datetime.datetime.strptime(s_start, "%Y/%m/%d").date() +
                                  datetime.timedelta(days=period)))

    end = stock['close'][0]
    start = stock['close'][len(stock)-1]

    return (end-start)/start


print(get_stock_rate('000651', '2017/01/01', 30))