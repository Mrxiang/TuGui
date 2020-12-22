import  akshare as ak
import datetime

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

#获取000001.SZ所属行业
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
class IndustryData():
    def __init__(self):
        pass
    def get_index_spot(self):
        df = ak.sw_index_spot()
        return df

    def get_index_cons(self, index_code):
        print( 'index_code', index_code)
        df = ak.sw_index_cons(index_code=index_code)
        return  df

    def get_index_daily(self , index_code, start_date, end_date):
        df=ak.sw_index_daily(index_code=index_code, start_date=start_date, end_date=end_date)
        return  df



if __name__ == '__main__':
    today_date = (datetime.date.today()).strftime('%Y-%m-%d')
    df_index= IndustryData().get_index_spot()
    print( df_index )
    for index, row in df_index.iterrows():
        print( 'index', index, 'row', row)
        df_cons= IndustryData().get_index_cons( row[0])
        print(df_cons)



