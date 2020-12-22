import  tushare as ts
from dateutil.relativedelta import relativedelta
from sqlalchemy import create_engine

# from Token import Token

from datetime import *
import datetime

class NewData():
    def __init__(self):
        super().__init__()  # 调用父类的初始化方法

    def get_new_share(self):
        today_date = (datetime.date.today()).strftime('%Y%m%d')
        last_date = (datetime.date.today() - relativedelta(months=+1)).strftime('%Y%m%d')
        pro = ts.pro_api('ac147953b15f6ee963c164fc8ee8ef5228e58b75e5953ba5997ef117')
        df = pro.new_share(start_date=last_date, end_date=today_date )
        # df= ts.new_stocks()
        print(df.shape, df.head())
        return  df

if __name__ == "__main__":
    # today_date = (datetime.date.today()).strftime('%Y-%m-%d')
    # print( 'today', today_date)
    df = NewData().get_new_share(  )
    engine = create_engine('sqlite:///new.db')
    print(df)
    df.to_sql('Macro'+'_'+'2020'+'_'+'3', engine, if_exists='replace')