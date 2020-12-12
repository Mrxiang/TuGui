

import tushare as ts
import  pandas as pd


class CBData():
    def __init__(self):
        pass
    def get_fund_data(self ):
        pro = ts.pro_api('***********')
        df = pro.cb_basic(fields="ts_code,bond_short_name,stk_code,stk_short_name,list_date,delist_date")

        return  df


if __name__ == "__main__":
    df = CBData().get_fund_data()
    print( df.head())


