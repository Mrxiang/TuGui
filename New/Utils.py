# IPO新股列表
#
# 接口：new_share
# 描述：获取新股上市列表数据
# 限量：单次最大2000条，总量不限制
# 积分：用户需要至少120积分才可以调取，具体请参阅积分获取办法
#
# 输入参数
# 名称 	类型 	必选 	描述
# start_date 	str 	N 	上网发行开始日期
# end_date 	str 	N 	上网发行结束日期
#
# 输出参数
# 名称 	类型 	默认显示 	描述
# ts_code 	str 	Y 	TS股票代码
# sub_code 	str 	Y 	申购代码
# name 	    str 	Y 	名称
# ipo_date 	str 	Y 	上网发行日期
# issue_date 	str 	Y 	上市日期
# amount 	float 	Y 	发行总量（万股）
# market_amount 	float 	Y 	上网发行总量（万股）
# price 	float 	Y 	发行价格
# pe 	    float 	Y 	市盈率
# limit_amount 	float 	Y 	个人申购上限（万股）
# funds 	float 	Y 	募集资金（亿元）
# ballot 	float 	Y 	中签率

NewDataUtils ={
    'ts_code':'股票代码',
    'sub_code': '申购代码',
    'name': '名称',
    'ipo_date': '上网发行日期',
    'issue_date': '上市日期',
    'amount': 	'发行总量（万股）',
    'market_amount': 	'上网发行总量（万股）',
    'price': 	'发行价格',
    'pe':	    '市盈率',
    'limit_amount': 	'个人申购上限（万股）',
    'funds': 	'募集资金（亿元）',
    'ballot': 	'中签率'
}