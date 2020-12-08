from tkinter import messagebox

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import  tushare as ts
import mpl_finance as mpf
from matplotlib.pylab import date2num
import datetime
from matplotlib.pylab import mpl
import matplotlib.pyplot as plt

class Application(Frame): #自己创建的这个类就是一个组件，这个要继承Frame类

    def __init__(self,master=None):  #参数  源码就是这样写，master代表的是父容器
        # Frame是父类，得主动的调用父类 的构造器
        super().__init__(master)   # super() 代表的是父类的定义，而不是父类的对象
        self.master = master
        # self.pack()  #这个组件的定位
        self.createWidget()  #自定义方法，在这个方法里自定义组件


# 以后就在这个方法里面自定义组件
    def createWidget(self):
#         创建组件
        self.btn01 = Button(self)
        self.btn01["text"] = "点击送花"
        self.btn01.pack()
        self.btn01["command"] = self.songhua

#         创建一个退出按钮
        self.btnquit = Button(self,text = "退出",command = root.destroy)
        self.btnquit.pack()

    def songhua(self):
        messagebox.showinfo("送花","送很多的花")


class MFrame( Frame):
    def __init__(self, root=None):
        super().__init__(root)
        self.root = root
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.f_plot = self.figure.add_subplot(111)
        self.canvs = FigureCanvasTkAgg(self.figure, self)
        self.canvs.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

    def draw_picture(self , code =None):
        if code ==1 :
            self.draw_picture1()
        if code ==2 :
            self.draw_picture2()
        if code ==3 :
            self.draw_picture3()


    def draw_picture1(self):
        self.f_plot.clear()
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #关于数据的部分可以提取出来
        y = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
        self.f_plot.plot(x, y)
        self.canvs.draw()

    def draw_picture2(self):
        self.f_plot.clear()
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #关于数据的部分可以提取出来
        y = [2, 4, 6, 8, 10, 8, 6, 4, 2, 0]
        self.f_plot.plot(x, y)
        self.canvs.draw()

    def draw_picture3(self):
        self.f_plot.clear()
        x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        y = [3, 6, 9, 12, 15, 18, 15, 12, 15, 18]
        self.f_plot.plot(x, y)
        self.canvs.draw()
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
        # ax.clear()
        # fig.subplots_adjust(bottom=0.2)
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

root = Tk()
root.title("tkinter and matplotlib")
mframe = MFrame( root )
mframe.pack()
button1 = Button(root, text='pic', command=lambda:mframe.draw_picture(1))
button1.pack()
button2 = Button(root, text='pic2', command=lambda:mframe.draw_picture(2))
button2.pack()
button3=Button(root, text='pic3', command=lambda:mframe.draw_picture(3))
button3.pack()
button4=Button(root, text='pic4', command=lambda:mframe.draw_kmatplotlib('000333'))
button4.pack()
button5=Button(root, text='pic5', command=lambda:mframe.draw_kmatplotlib('000001'))
button5.pack()
app = Application(master = root)
app.pack()
root.mainloop()

