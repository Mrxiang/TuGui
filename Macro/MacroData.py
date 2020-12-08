
import  tushare as ts

pro = ts.pro_api('***********')

df = pro.cn_m(start_m='201901', end_m='202003')
print( df )
#获取指定字段
# df = pro.cn_m(start_m='201901', end_m='202003', fields='month,m0,m1,m2')