import tushare as ts
from dateutil.relativedelta import relativedelta
import pandas as pd
import datetime


class HKData():
    def __init__(self):
        super().__init__()
        self.pro = ts.pro_api('ac147953b15f6ee963c164fc8ee8ef5228e58b75e5953ba5997ef117')
        ts.set_token('ac147953b15f6ee963c164fc8ee8ef5228e58b75e5953ba5997ef117')
        self.stock_basic= self.pro.stock_basic()
    def get_hk_data(self):
        today = (datetime.date.today() -relativedelta(days=+1)).strftime('%Y%m%d')
        df = self.pro.hk_hold(trade_date=today)
        return  df
if __name__ == '__main__':
    today = (datetime.date.today() - relativedelta(days=+1)).strftime('%Y%m%d')
    df=HKData().get_hk_data()
    print( df )