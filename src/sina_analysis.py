import tushare_wrapper as tuw
import pymysql

class SinaAnalysis:

    def __init__(self):
        config = open('config.txt').readlines()
        db_user = str(config[0][config[0].index('=') + 1:]).strip()
        db_password = str(config[1][config[1].index('=') + 1:]).strip()
        db_path = str(config[2][config[2].index('=') + 1:]).strip()
        db_name = str(config[3][config[3].index('=') + 1:]).strip()
        self.conn = pymysql.connect(host=db_path, user=db_user, password=db_password, db=db_name)
        self.cursor = self.conn.cursor()

    def GetSpecificDateStockUpData(self, date, afterdays=10):
        querysql = "Select stock_code from analysis where date_time='{0}'".format(date)
        self.cursor.execute(querysql)
        for item in self.cursor.fetchall():
            print(str(item)[2:8])
            print(tuw.get_stock_rate(str(item)[2:8], date.replace('-','/'), workdays=afterdays))

    def GetMostRecommandStock(self, num):
        querysql = "Select stock_code ,count(*) from analysis group by stock_code order by count(*) desc limit {0}".format(num)
        self.cursor.execute(querysql)

        rtn = ""
        for item in self.cursor.fetchall():
            rtn = rtn + str(item)[2:8] + "|"
        return rtn

a = SinaAnalysis()
print(a.GetSpecificDateStockUpData(date='2017-08-01'))