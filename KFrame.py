
from tkinter import *
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.pylab import date2num
import datetime
import  tushare as ts
import mpl_finance as mpf

class KFrame(Frame):
    """一个经典的GUI写法"""

    def __init__(self, root=None, code = None):
        '''初始化方法'''
        super().__init__(root)  # 调用父类的初始化方法
        self.root = root
        # self.pack(side=TOP, fill=BOTH, expand=1)  # 此处填充父窗体
        self.label = Label(self.root, text='这是一个Tkinter和Matplotlib相结合的小例子')
        self.label.pack()
        self.canvas = Canvas()  # 创建一块显示图形的画布
        self.draw_matplotlib(code)

    def draw_matplotlib(self, code=None):
        """创建绘图对象"""
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
        self.figure = plt.figure(figsize=(24, 15))
        self.figure.clf()
        # ax = self.figure.subplots()
        ax = self.figure.add_subplot(111)
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
        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas.draw()

    def destroy(self):
        """重写destroy方法"""
        super().destroy()
        # quit()

    def quit(self):
        """点击退出按钮时调用这个函数"""
        root.quit()  # 结束主循环
        root.destroy()  # 销毁窗口


if __name__ == '__main__':
    root = Tk()
    root.title('数学曲线窗口')
    root.geometry('560x400+200+200')
    app = KFrame(root=root, code='000333')
    app.pack()
    root.mainloop()