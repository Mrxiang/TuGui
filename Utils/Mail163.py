# coding=utf-8
import smtplib  # smtp服务器
from email.mime.text import MIMEText  # 邮件文本
import pandas as pd
import numpy as np
from email.mime.multipart import MIMEMultipart
import tushare as ts
from email.header import Header
from email.mime.application import MIMEApplication
import datetime
# 邮件构建
today_date = (datetime.date.today()).strftime('%Y%m%d')


class Mail:
    def __init__(self):
        super().__init__()  # 调用父类的初始化方法

    def send_email(title, df ):


        sender = 'xsx0721@163.com'  # 发送方
        recver = ['458826119@qq.com','285022155@qq.com','xsx0721@163.com']  # 接收方
        password = "TSVSWNMMIHUDHUYY"

        # message = MIMEMultipart()  # 创建一个带附件的实例
        content=df.to_string()
        # content=df.to_markdown()
        print(content)
        message = MIMEText(content, 'plain', 'utf-8')
        message['To'] = Header(",".join(recver))  # 收件人
        message['From'] = sender  # 发件人
        message["Subject"] = Header(title, 'utf-8').encode()  # 指定邮件主题

        # zengjiafuain
        # message.attach(MIMEText('附件为xxxxx执行结果,请查收!', _subtype='html', _charset='utf-8'))
        # part = MIMEApplication(open(filename, 'rb').read())
        # part.add_header('Content-Disposition', 'attachment', filename=filename)
        # message.attach(part)

        smtp = smtplib.SMTP_SSL("smtp.163.com", 994)  # 实例化smtp服务器
        smtp.login(sender, password)  # 发件人登录
        smtp.sendmail(sender, recver, message.as_string())  # as_string 对 message 的消息进行了封装
        smtp.close()


if __name__ == "__main__":
    today_date = (datetime.date.today()).strftime('%Y%m%d')
    print(today_date)
    pro = ts.pro_api('ac147953b15f6ee963c164fc8ee8ef5228e58b75e5953ba5997ef117')
    forecast = pro.forecast(ann_date=today_date)
    basic =pro.stock_basic()
    df=pd.merge(forecast,basic, on='ts_code', how='left')
    df=df.drop('symbol', axis=1)
    order = ['ts_code', 'name', 'area', 'industry', 'market', 'list_date', 'ann_date', 'end_date', 'type',
             'p_change_min', 'p_change_max', 'net_profit_min', 'net_profit_max', 'last_parent_net', 'first_ann_date',
             'summary', 'change_reason']
    df=df[order]
    df=df.sort_values(by='p_change_min',ascending=False)
    df.reset_index(drop=True, inplace=True)
    df.columns=['代码','名称','地域','行业','市场类型','上市日期','公告日期','报告期','业绩类型','净利润浮动下限','净利润浮动上限','预告净利润下限','预告净利润上限','上年同期归母净利润','首次公告日','业绩预告摘要','业绩变动原因']
    df['|']='                '
    Mail.send_email( today_date+"业绩快报",df )
    print("发送成功")

    yesterday = (datetime.date.today() - datetime.timedelta(days=1)).strftime('%Y%m%d')
    news = pro.cctv_news(date=yesterday)
    Mail.send_email(yesterday+"新闻联播", news )
    print("发送成功")


    new_share=pro.new_share(start_date=today_date)
    Mail.send_email(today_date+"申购", new_share)
    print("发送成功")
# order=['ts_code', 'name', 'area','industry', 'market', 'list_date','ann_date', 'end_date', 'type', 'p_change_min', 'p_change_max', 'net_profit_min', 'net_profit_max', 'last_parent_net', 'first_ann_date', 'summary', 'change_reason', 'symbol' ]
# stock_basic
# ts_code	str	Y	TS代码
# symbol	str	Y	股票代码
# name	str	Y	股票名称
# area	str	Y	地域
# industry	str	Y	所属行业
# market	str	Y	市场类型（主板/创业板/科创板/CDR）
# list_date	str	Y	上市日期

# forecast
# ts_code	str	TS股票代码
# ann_date	str	公告日期
# end_date	str	报告期
# type	str	业绩预告类型(预增/预减/扭亏/首亏/续亏/续盈/略增/略减)
# p_change_min	float	预告净利润变动幅度下限（%）
# p_change_max	float	预告净利润变动幅度上限（%）
# net_profit_min	float	预告净利润下限（万元）
# net_profit_max	float	预告净利润上限（万元）
# last_parent_net	float	上年同期归属母公司净利润
# first_ann_date	str	首次公告日
# summary	str	业绩预告摘要
# change_reason	str	业绩变动原因
# df.columns=['代码','代码','名称','地域','行业','市场类型','上市日期','公告日期','报告期','业绩类型','净利润浮动下限','净利润浮动上限','预告净利润下限','预告净利润下限','上年同期归母净利润','首次公告日','业绩预告摘要','业绩变动原因']