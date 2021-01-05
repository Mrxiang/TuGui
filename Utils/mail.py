# coding=utf-8
import smtplib  # smtp服务器
from email.mime.text import MIMEText  # 邮件文本
import pandas as pd
import numpy as np

import tushare as ts

# 邮件构建
def send_email(df_values ):
    subject = "title"  # 邮件标题
    sender = "xxxxxxx"  # 发送方
    content = str(df_values)
    recver = "xxxxxxx"  # 接收方
    password = "TSVSWNMMIHUDHUYY"
    message = MIMEText(content, "plain", "utf-8")
    # content 发送内容     "plain"文本格式   utf-8 编码格式

    message['Subject'] = subject  # 邮件标题
    message['To'] = recver  # 收件人
    message['From'] = sender  # 发件人

    smtp = smtplib.SMTP_SSL("smtp.163.com", 994)  # 实例化smtp服务器
    smtp.login(sender, password)  # 发件人登录
    smtp.sendmail(sender, [recver], message.as_string())  # as_string 对 message 的消息进行了封装
    smtp.close()

if __name__ == "__main__":
    df= pd.DataFrame( np.arange(10))
    send_email(df.values)
