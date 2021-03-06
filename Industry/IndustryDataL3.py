import datetime
from dateutil.relativedelta import relativedelta
import  tushare as ts
import  pandas as pd
#获取申万一级行业列表
# df = pro.index_classify(level='L1', src='SW')
#
# 获取申万二级行业列表
# df = pro.index_classify(level='L2', src='SW')
#
# 获取申万三级级行业列表
# df = pro.index_classify(level='L3', src='SW')
#
#
# 获取黄金分类的成份股
# df = pro.index_member(index_code='850531.SI')

#获取000001. ndvm,nvddnddnnnns,dsldmsdlmsdms.dmslmdlsmldfkfnsdkjiesddekdndvnjdlvndjknjkddkkkkkkkkkkmmmmmmmmmmmmmmmmmmmmmmm                                                                                                                                     v g                                         sSZ所属行业
# df = pro.index_member(ts_code='000001.SZ')

#获取深圳市场20200320各板块交易数据
# df = pro.daily_info(trade_date='20200320', exchange='SZ')

#获取深圳和上海市场20200320各板块交易指定字段的数据
# df = pro.daily_info(trade_date='20200320', exchange='SZ,SH', fields='trade_date,ts_name,pe')

# 申万一级行业实时行情
# sw_index_spot_df = ak.sw_index_spot()
# 申万一级行业成份
# sw_index_df = ak.sw_index_cons(index_code="801010")
# 申万一级行业历史行情
# sw_index_df = ak.sw_index_daily(index_code="801010", start_date="2019-12-01", end_date="2019-12-07")
class IndustryDataL3():
    def __init__(self):
        super().__init__()
        self.pro = ts.pro_api('ac147953b15f6ee963c164fc8ee8ef5228e58b75e5953ba5997ef117')
        self.basic = self.pro.stock_basic()
    # 获取三级行业分类
    def get_index_spot(self):

        df = self.pro.index_classify(level='L3', src='SW')
        return df
    # 获取行业成分
    def get_index_cons(self, index_code):
        print( 'index_code', index_code)
        df= self.pro.index_member(index_code=index_code)
        df.rename(columns={'con_code':'ts_code'},inplace='True')
        df= pd.merge(df, self.basic, how='left', on='ts_code')
        return  df
    # 获取行业指数
    # def get_index_daily(self , index_code, start_date=0, end_date=0):
    #     if end_date==0:
    #         end_date = (datetime.date.today()).strftime('%Y%m%d')
    #     if start_date ==0:
    #         start_date = (datetime.date.today() - relativedelta(years=+1)).strftime('%Y%m%d')
    #     df=ak.sw_index_daily(index_code=index_code, start_date=start_date, end_date=end_date)
    #     return  df
    # 获取成分历史记录
    def get_cons_history(self, code):
        pass

if __name__ == '__main__':
    start_date = (datetime.date.today()).strftime('%Y%m%d')
    end_date = (datetime.date.today() - relativedelta(years=+1)).strftime('%Y%m%d')
    df_index= IndustryDataL3().get_index_spot()
    print( df_index )
    for index, row in df_index.iterrows():
        print( 'index', index, 'row', row)
        df_cons= IndustryDataL3().get_index_cons( row[0])
        print(df_cons)
        # df_daily = IndustryDataL3().get_index_daily( index_code=row[0],  start_date=start_date, end_date=end_date)
        # print( df_daily )


