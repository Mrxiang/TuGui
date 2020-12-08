

import tushare as ts
import  pandas as pd

def get_cb_data():
    pro = ts.pro_api('***********')
    # 获取可转债基础信息列表
    df = pro.cb_basic(fields="ts_code,bond_short_name,stk_code,stk_short_name,list_date,delist_date")
    print('可转债', df.shape)


if __name__ == "__main__":
    df = get_cb_data()


