


import tushare as ts
import pandas as pd
import datetime


pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
# 1 获取列表


pro = ts.pro_api('ac147953b15f6ee963c164fc8ee8ef5228e58b75e5953ba5997ef117')

golden = pro.broker_recommend(month='202107')


profit=0
mean_profit=0
for idx, row in golden.iterrows():
    print(idx, row)
    ts_code= row['ts_code']
    result= df = pro.daily(ts_code=ts_code, start_date='20210701', end_date='20210801')
    print(result)
    # print(result.columns)
    profit +=(result.iloc[0].close -  result.iloc[-1].close)
    mean_profit += (result['close'].mean() - result.iloc[-1].close)
    print( " profit ",profit," mean_profit ", mean_profit)
    # break


print( "month profit  ",profit, " month mean profit ",profit, mean_profit )