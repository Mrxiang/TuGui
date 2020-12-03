import math
import numpy as np
# -------------------------------------------------------------------------------------------
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk  # NavigationToolbar2TkAgg
# ------------------------------------------------------------------------------------------
import tkinter as tk
import  tushare as ts
# ------------------------------------------------------------------------------------------
import mpl_finance as mpf
from matplotlib.pylab import date2num
import datetime
from tkinter import  *
from matplotlib.figure import Figure


class MatFrame(Frame):
    def __init__(self, root =None):
        super().__init__(root)
        self.root =  root  # 创建主窗体
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.f_plot = self.figure.add_subplot(111)
        self.canvs = FigureCanvasTkAgg(self.figure, self)
        self.canvs.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


    def draw_matplotlib(self, code=None):
        # 设置中文显示字体
        mpl.rcParams['font.sans-serif'] = ['SimHei']  # 中文显示
        mpl.rcParams['axes.unicode_minus'] = False  # 负号显示
        # 创建绘图对象f figsize的单位是英寸 像素 = 英寸*分辨率
        """ 
        """
        dh = ts.get_hist_data(code)
        df = dh.sort_values(by='date')
        print(df.head())
        df = df[df.index > '2020-01-01']
        # if len(df) < 10:
        #     print(" len(df) <10 ")
        #     sys.exit(2)

        # 对tushare获取到的数据转换成 candlestick_ohlc()方法可读取的格式
        alist = []
        tlist = []
        for date, row in df.iterrows():
            open, high, close, low, volume, price_change, p_change, ma5, ma10, ma20, v_ma5, v_ma10, v_ma20 = row[0:13]
            # 将日期转换为数字
            date1 = datetime.datetime.strptime(date, '%Y-%m-%d')
            t = date2num(date1)
            data = (t, open, high, low, close)
            alist.append(data)
            tlist.append(t)

        # 加这个两句 可以显示中文
        plt.rcParams['font.sans-serif'] = [u'SimHei']
        plt.rcParams['axes.unicode_minus'] = False

        # 设置X轴刻度为日期时间
        self.f_plot.clear()
        self.f_plot.xaxis_date()
        self.f_plot.autoscale_view()
        # plt.setp(plt.gca().get_xticklabels(), rotation=45)
        plt.xticks(rotation=45)
        plt.yticks()
        plt.title(" {0}".format(code))
        plt.xlabel("date")
        plt.ylabel("price")
        mpf.candlestick_ohlc(self.f_plot, alist, colorup='red', colordown='green')
        #  画 10,20日均线
        plt.plot(tlist, df['ma10'].values, 'blue', label='ma10')
        plt.plot(tlist, df['ma20'].values, 'g--', label='ma20')
        plt.legend(loc='best', shadow=True)
        plt.grid()
        self.canvs.draw()

if __name__ == "__main__":
    form = MatFrame()