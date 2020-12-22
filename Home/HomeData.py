

import  tushare as ts
from sqlalchemy import create_engine

# from Token import Token

from datetime import *
import datetime

class HomeData():
    def __init__(self):
        super().__init__()  # 调用父类的初始化方法

    def get_today_all(self):
        # pro = ts.pro_api('***********')
        df = ts.get_today_all( )
        print(df.shape, df.head())
        return  df

if __name__ == "__main__":
    # today_date = (datetime.date.today()).strftime('%Y-%m-%d')
    today_date = (datetime.date.today()).strftime('%Y%m%d')
    print( 'today', today_date)
    df = HomeData().get_today_all( )
    engine = create_engine('sqlite:///home.db')
    print(df)
    df.to_sql('Macro'+'_'+'2020'+'_'+'3', engine, if_exists='replace')