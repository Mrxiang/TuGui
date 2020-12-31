# MACD的红绿柱表bai示的是DIFF与DEA之间du的距离。
#
# DIFF<DEA时为绿柱，DIFF>DEA时为红柱zhi。
#
# MACD红柱代表dao价格将低位回升或进一步zhuan上扬，对应走势通常呈单边上行，是多头动能持续累积的信号，且盘面以多头行情为主导。
# MACD绿柱代表价格将高位回调或进一步下行，对应走势通常呈单边下行，是空头动能持续累积的信号，且盘面以空头行情为主导。

import pandas as pd
import  numpy as np
from pandas import DataFrame
import pylab as plt
import  tushare as ts

# MACD的红绿柱表bai示的是DIFF与DEA之间du的距离。
#
# DIFF<DEA时为绿柱，DIFF>DEA时为红柱zhi。
#
# MACD红柱代表dao价格将低位回升或进一步zhuan上扬，对应走势通常呈单边上行，是多头动能持续累积的信号，且盘面以多头行情为主导。
# MACD绿柱代表价格将高位回调或进一步下行，对应走势通常呈单边下行，是空头动能持续累积的信号，且盘面以空头行情为主导。
def get_macd(df):
    print('length ', len(df), 'shape ',df.shape)
    _columns_ = ['EMA_12', 'EMA_26', 'DIFF', 'MACD', 'BAR']
    a = np.zeros(len(df) * 5).reshape(len(df), 5)  # 也可以EMA_12 = [0 for i in range(len(df))]
    print('df ', df.head(10))
    a[-1][0] = df['close'][0]  # EMA_12
    a[-1][1] = df['close'][0]
    print( a[-1][0],a[-1][1] )
    for i in range(len(df)):
        a[i][0] = a[i - 1][0] * 11 / 13 + df['close'][i] * 2 / 13  # EMA_12
        a[i][1] = a[i - 1][1] * 25 / 27 + df['close'][i] * 2 / 27  # EMA_26
        a[i][2] = a[i][0] - a[i][1]  # DIFF
        a[i][3] = a[i - 1][3] * 8 / 10 + a[i][2] * 2 / 10  # MACD
        a[i][4] = 2 * (a[i][2] - a[i][3])
    return DataFrame(a, index=df.index, columns=_columns_)

def plt_macd(df,da):
    my_dfs = [
        # df['open'],
        # da['EMA_12'],
        # da['EMA_26'],
        # da['DIFF'],
        da['MACD'],
        da['BAR'],
    ] # or in your case [ df,do]
    my_opts = [
                # {"color":"green", "linewidth":1.0, "linestyle":"-","label":"open"},
                # {"color":"blue","linestyle":"-","label":"EMA_12"},
                # {"color":"yellow","linestyle":"-","label":"EMA_26"},
                # {"color":"black","linestyle":"-","label":"DIFF"},
                {"color":"red","linestyle":"-","label":"MACD"},
                {"color":"orange","linestyle":"-","label":"BAR"}
    ]
    for d,opt in zip(my_dfs, my_opts):
        d.plot( **opt)
    plt.grid()
    plt.legend(loc=0)
    plt.show()

if __name__ == '__main__':
    # df = ts.get_hist_data('300911',start='2020-11-01',end='2020-12-16')
    pro = ts.pro_api('ac147953b15f6ee963c164fc8ee8ef5228e58b75e5953ba5997ef117')
    df = pro.index_daily(ts_code='000333.SZ', start_date='20201101', end_date='20201216')
    df=df.sort_values(by='trade_date')
    da = get_macd(df)
    print( da.head(10) )

    plt_macd(df,da)