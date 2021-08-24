
from tkinter import  *
from apscheduler.schedulers.background import BackgroundScheduler

from Utils.Mail163 import Mail


class MainFrame(Frame ):
    def __init__(self, root=None):
        super().__init__(root)  # 调用父类的初始化方法
        self.root = root
        self.schedul_work()

    def schedul_work(self):
        scheduler = BackgroundScheduler()
        print('begin schedule job')
        scheduler.add_job(job, 'cron', day_of_week='1,2,3,4,5', hour='16')
        print('begin schedule job2')
        scheduler.add_job(job2, 'cron', minute='0-59')
        scheduler.start()

def job():
    print("I'm working... in job1  ")
    Mail.send_email('复盘')

def job2():
    print("I'm working... in job2")
