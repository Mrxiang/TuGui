
import  tushare as ts
from sqlalchemy import create_engine

from Token import Token

pro = ts.pro_api('ac147953b15f6ee963c164fc8ee8ef5228e58b75e5953ba5997ef117')

df = pro.cn_m(start_m='201901', end_m='202003')
print( df )

class MacroData(Token):
    def __init__(self):
        super().__init__()  # 调用父类的初始化方法
    def get_cn_m(self):
        df = pro.cn_m(start_m='201901', end_m='202003')
        print(df)
        return  df

if __name__ == "__main__":
    df = MacroData.get_cn_m()
    engine = create_engine('sqlite:///macro.db')
    print(df)
    df.to_sql('Macro'+'_'+'2020'+'_'+'3', engine, if_exists='replace')