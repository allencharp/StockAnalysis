import pymysql
import gevent
import tushare_wrapper as tuw
import datetime
from datetime import timedelta

class SinaCalcul:

    def __init__(self):
        config = open('config.txt').readlines()
        db_user = str(config[0][config[0].index('=') + 1:]).strip()
        db_password = str(config[1][config[1].index('=') + 1:]).strip()
        db_path = str(config[2][config[2].index('=') + 1:]).strip()
        db_name = str(config[3][config[3].index('=') + 1:]).strip()
        self.conn = pymysql.connect(host=db_path, user=db_user, password=db_password, db=db_name)
        self.cursor = self.conn.cursor()

    def Insert10daysScore(self,date=(datetime.datetime.now()-timedelta(days=10)).strftime("%Y-%m-%d")):

        querysql = "Select item, stock_code from analysis where date_time<'{0}'".format(date)
        self.cursor.execute(querysql)
        for item in self.cursor.fetchall():
            print(str(item))
            print(item[1])
            print(tuw.get_stock_rate(item[0], date.replace('-', '/'), workdays=10))


a = SinaCalcul()
print(a.Insert10daysScore())