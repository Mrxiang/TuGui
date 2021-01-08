
import  tushare as ts
from sqlalchemy import create_engine
import datetime
from Token import Token
from dateutil.relativedelta import relativedelta


class MacroData(Token):
    def __init__(self):
        super().__init__()  # 调用父类的初始化方法
        self.pro = ts.pro_api('ac147953b15f6ee963c164fc8ee8ef5228e58b75e5953ba5997ef117')

    def get_cn_m(self, start_m, end_m):
        df_m = self.pro.cn_m(start_m=start_m, end_m=end_m)
        print(df_m)
        return  df_m

if __name__ == "__main__":
    end_m = (datetime.date.today()).strftime('%Y%m')
    start_m=(datetime.date.today()-relativedelta(years=+10)).strftime('%Y%m')
    df = MacroData().get_cn_m(start_m, end_m)
    df.to_csv(start_m+'_m.csv')
    print(df)
