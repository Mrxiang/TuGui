

# 输出参数

# 名称	类型	默认显示	描述
# ts_code	str	Y	转债代码
# bond_full_name	str	Y	转债名称
# bond_short_name	str	Y	转债简称
# cb_code	str	Y	转股申报代码
# stk_code	str	Y	正股代码
# stk_short_name	str	Y	正股简称
# maturity	float	Y	发行期限（年）
# par	float	Y	面值
# issue_price	float	Y	发行价格
# issue_size	float	Y	发行总额（元）
# remain_size	float	Y	债券余额（元）
# value_date	str	Y	起息日期
# maturity_date	str	Y	到期日期
# rate_type	str	Y	利率类型
# coupon_rate	float	Y	票面利率（%）
# add_rate	float	Y	补偿利率（%）
# pay_per_year	int	Y	年付息次数
# list_date	str	Y	上市日期
# delist_date	str	Y	摘牌日
# exchange	str	Y	上市地点
# conv_start_date	str	Y	转股起始日
# conv_end_date	str	Y	转股截止日
# first_conv_price	float	Y	初始转股价
# conv_price	float	Y	最新转股价
# rate_clause	str	Y	利率说明
# put_clause	str	N	赎回条款
# maturity_put_price	str	N	到期赎回价格(含税)
# call_clause	str	N	回售条款
# reset_clause	str	N	特别向下修正条款
# conv_clause	str	N	转股条款
# guarantor	str	N	担保人
# guarantee_type	str	N	担保方式
# issue_rating	str	N	发行信用等级
# newest_rating	str	N	最新信用等级
# rating_comp	str	N	最新评级机构