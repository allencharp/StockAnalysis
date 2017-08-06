import tushare as ts
from dateutil import parser
import datetime


def get_stock_rate(s_code, s_start, workdays):
    try:
        stock = ts.get_h_data(code=s_code, autype="hfq", start=s_start,
                              end=str(datetime.datetime.strptime(s_start, "%Y/%m/%d").date() +
                                      datetime.timedelta(days=workdays)))

        end = stock['close'][0]
        start = stock['close'][len(stock)-1]
    except:
        return 0
    return (end-start)/start


print(get_stock_rate('300087', '2017/07/28', 1))