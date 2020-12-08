# 输入参数
#
# 名称	类型	必选	描述
# market	str	N	交易市场: E场内 O场外（默认E）
# status	str	N	存续状态 D摘牌 I发行 L上市中
# 输出参数
#
# 名称	类型	默认显示	描述
# ts_code	str	Y	基金代码
# name	str	Y	简称
# management	str	Y	管理人
# custodian	str	Y	托管人
# fund_type	str	Y	投资类型
# found_date	str	Y	成立日期
# due_date	str	Y	到期日期
# list_date	str	Y	上市时间
# issue_date	str	Y	发行日期
# delist_date	str	Y	退市日期
# issue_amount	float	Y	发行份额(亿)
# m_fee	float	Y	管理费
# c_fee	float	Y	托管费
# duration_year	float	Y	存续期
# p_value	float	Y	面值
# min_amount	float	Y	起点金额(万元)
# exp_return	float	Y	预期收益率
# benchmark	str	Y	业绩比较基准
# status	str	Y	存续状态D摘牌 I发行 L已上市
# invest_type	str	Y	投资风格
# type	str	Y	基金类型
# trustee	str	Y	受托人
# purc_startdate	str	Y	日常申购起始日
# redm_startdate	str	Y	日常赎回起始日
# market	str	Y	E场内O场外