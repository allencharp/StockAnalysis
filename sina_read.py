
from pyquery import PyQuery as pq
import pymysql
import gevent
import datetime

class SinaStockModel:

    def __init__(self):
        stock_code = ""
        stock_name = ""
        target_price = ""
        rating = ""
        organization = ""
        analyst = ""
        market = ""
        date_time = ""

class SinaData:

    def __init__(self):
        config = open('/Users/allen/desktop/stock/config.txt').readlines()
        db_user = str(config[0][config[0].index('=')+1:]).strip()
        db_password = str(config[1][config[1].index('=')+1:]).strip()

        self.analURL = "http://vip.stock.finance.sina.com.cn/q/go.php/vIR_RatingNewest/index.phtml?p={0}"
        self.conn = pymysql.connect(host="127.0.0.1", user=db_user, password=db_password, db='allen')
        self.cursor = self.conn.cursor()
        self.conn.set_charset('utf8')
        self.cursor.execute('SET NAMES utf8;')
        self.cursor.execute('SET CHARACTER SET utf8;')
        self.cursor.execute('SET character_set_connection=utf8;')

    def __del__(self):
        self.cursor.close()
        self.conn.close()


    def ReadData(self):
        jobs = [gevent.spawn(self.ReadPageData, page) for page in range(1,20)]
        gevent.joinall(jobs)

    def ReadPageData(self, page):
        respyquery = pq(url=self.analURL.format(page))
        stock_info = respyquery('tr')
        for i in range(1, len(stock_info)):
            item = SinaStockModel()
            item.stock_code = (stock_info("td").eq(13 * i).text())
            item.stock_name = (stock_info("td").eq(13 * i + 1).text().encode("latin1").decode('gbk'))
            item.target_price = (stock_info("td").eq(13 * i + 2).text())
            item.rating = (stock_info("td").eq(13 * i + 3).text().encode("latin1").decode('gbk'))
            item.organization = (stock_info("td").eq(13 * i + 4).text().encode("latin1").decode('gbk'))
            item.analyst = (stock_info("td").eq(13 * i + 5).text().encode("latin1").decode('gbk'))
            item.market = (stock_info("td").eq(13 * i + 6).text().encode("latin1").decode('gbk'))
            item.date_time = (stock_info("td").eq(13 * i + 7).text())
            if item.date_time == datetime.datetime.now().strftime("%Y-%m-%d"):
                self.SaveData(item)

        self.conn.commit()

    def SaveData(self, item):

        insertquery = "INSERT INTO analysis " \
            "(stock_code, stock_name, target_price, rating, organization, analyst, market, date_time) "\
            "VALUE ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')"\
            .format(item.stock_code, item.stock_name, item.target_price, item.rating, item.organization, item.analyst,
                    item.market, item.date_time)
        print(insertquery)
        self.cursor.execute(insertquery)



sina = SinaData()
sina.ReadData()
