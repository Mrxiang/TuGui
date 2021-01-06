
import datetime
from dateutil.relativedelta import relativedelta
import tushare as ts
from dateutil.relativedelta import relativedelta
import pandas as pd
class TrendData():
    def __init__(self):
        super().__init__()
        self.pro = ts.pro_api('ac147953b15f6ee963c164fc8ee8ef5228e58b75e5953ba5997ef117')
        # ac147953b15f6ee963c164fc8ee8ef5228e58b75e5953ba5997ef117
        ts.set_token('ac147953b15f6ee963c164fc8ee8ef5228e58b75e5953ba5997ef117')
    def get_trend_data(self):
        result_df = pd.DataFrame()
        today = (datetime.date.today()- relativedelta(days=+1)).strftime('%Y%m%d')
        start_date = (datetime.date.today() - relativedelta(years=+1)).strftime('%Y%m%d')

        basic = self.pro.daily_basic(trade_date=today)
        print( basic )
        for index, row in basic.iterrows():
            print( index, row )
            df = ts.pro_bar(ts_code=row.ts_code, start_date=start_date, end_date=today, ma=[5, 20, 30])
            # print( df.columns,df)
            one_df=df.head(1)
            if (one_df.loc[0].low < one_df.loc[0].ma5) and (one_df.loc[0].ma5 < one_df.loc[0].high) and (one_df.loc[0].low < one_df.loc[0].ma20) and (one_df.loc[0].ma20< one_df.loc[0].high):
                one_df['density']=0
            else :
                one_df['density']= (one_df.loc[0].ma5 +one_df.loc[0].ma20+one_df.loc[0].ma30)/one_df.close -3

            result_df=  result_df.append( one_df)

        return  result_df





if __name__ == '__main__':
    today = (datetime.date.today() - relativedelta(days=+1)).strftime('%Y%m%d')
    result=TrendData().get_trend_data()
    print( result.shape, result )
    result.to_csv(today+"trend_data.csv")


