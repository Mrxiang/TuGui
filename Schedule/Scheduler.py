# coding=utf-8

import schedule
import time
import datetime
#引入schedule和time
from Utils.Mail163 import Mail;

def forecast_job():
    print("send forecast ")
    today_date = (datetime.date.today()).strftime('%Y%m%d')
    Mail.send_email( today_date )
#定义一个叫job的函数，函数的功能是打印'I'm working...'

# schedule.every(10).minutes.do(job)       #部署每10分钟执行一次job()函数的任务
# schedule.every().hour.do(job)            #部署每×小时执行一次job()函数的任务
schedule.every().day.at("09:05").do(forecast_job) #部署在每天的10:30执行job()函数的任务
# schedule.every().monday.do(job)          #部署每个星期一执行job()函数的任务
# schedule.every().wednesday.at("13:15").do(job)#部署每周三的13：15执行函数的任务

while True:
    print("one minute...")
    schedule.run_pending()
    time.sleep(60)
#13-15都是检查部署的情况，如果任务准备就绪，就开始执行任务。