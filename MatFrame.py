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


class MatFrame:
    def __init__(self, root =None, code= None):
        self.root =  root  # 创建主窗体
        self.canvas = tk.Canvas()  # 创建一块显示图形的画布
        # self.draw_matplotlib()
        self.draw_kmatplotlib(code)

    def draw_matplotlib(self ):
        # 创建绘图对象f
        plt.clf()
        figure = plt.figure(num=2, figsize=(16, 12), dpi=80, facecolor="pink", edgecolor='green', frameon=True)
        # 创建一副子图
        fig1 = plt.subplot(1, 1, 1)

        x = np.arange(0, 2 * np.pi, 0.1)
        y1 = np.sin(x)
        y2 = np.cos(x)

        line1, = fig1.plot(x, y1, color='red', linewidth=3, linestyle='--')  # 画第一条线
        line2, = fig1.plot(x, y2)
        plt.setp(line2, color='black', linewidth=8, linestyle='-', alpha=0.3)  # 华第二条线

        fig1.set_title("这是第一幅图", loc='center', pad=20, fontsize='xx-large', color='red')  # 设置标题
        line1.set_label("正弦曲线")  # 确定图例
        fig1.legend(['正弦', '余弦'], loc='upper left', facecolor='green', frameon=True, shadow=True, framealpha=0.5,
                    fontsize='xx-large')

        fig1.set_xlabel('横坐标')  # 确定坐标轴标题
        fig1.set_ylabel("纵坐标")
        fig1.set_yticks([-1, -1 / 2, 0, 1 / 2, 1])  # 设置坐标轴刻度
        fig1.grid(which='major', axis='x', color='r', linestyle='-', linewidth=2)  # 设置网格

        # 把绘制的图形显示到tkinter窗口上
        self.canvas = FigureCanvasTkAgg(figure, self.root)
        self.canvas.draw()  # 以前的版本使用show()方法，matplotlib 2.2之后不再推荐show（）用draw代替，但是用show不会报错，会显示警告
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

        # 把matplotlib绘制图形的导航工具栏显示到tkinter窗口上
        toolbar = NavigationToolbar2Tk(self.canvas,self.root)  # matplotlib 2.2版本之后推荐使用NavigationToolbar2Tk，若使用NavigationToolbar2TkAgg会警告
        toolbar.update()
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def draw_kmatplotlib(self, code=None):
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

        # 创建子图
        # plt.clear()
        self.figure = plt.figure(figsize=(24, 15))

        self.figure.clf()
        ax = self.figure.subplots()
        # ax.clear()
        # fig.subplots_adjust(bottom=0.2)
        # 设置X轴刻度为日期时间
        ax.xaxis_date()
        ax.autoscale_view()
        # plt.setp(plt.gca().get_xticklabels(), rotation=45)
        plt.xticks(rotation=45)
        plt.yticks()
        plt.title(" {0}".format(code))
        plt.xlabel("date")
        plt.ylabel("price")
        mpf.candlestick_ohlc(ax, alist, colorup='red', colordown='green')
        #  画 10,20日均线
        plt.plot(tlist, df['ma10'].values, 'blue', label='ma10')
        plt.plot(tlist, df['ma20'].values, 'g--', label='ma20')
        plt.legend(loc='best', shadow=True)
        plt.grid()
        self.canvas = FigureCanvasTkAgg(self.figure, self.root)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas.draw()
if __name__ == "__main__":
    form = MatFrame()