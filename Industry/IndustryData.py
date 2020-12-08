



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