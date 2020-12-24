import datetime
from tkinter import  *
from tkinter import messagebox, ttk

from Industry.IndustryData import IndustryData
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pylab import mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.pylab import mpl
import mpl_finance as mpf
from matplotlib.pylab import date2num


class IndustryFrame(Frame): #自己创建的这个类就是一个组件，这个要继承Frame类

    def __init__(self, master=None):  # 参数  源码就是这样写，master代表的是父容器
        # Frame是父类，得主动的调用父类 的构造器
        super().__init__(master)  # super() 代表的是父类的定义，而不是父类的对象
        self.master = master
        # self.pack()  #这个组件的定位
        self.createWidget()  # 自定义方法，在这个方法里自定义组件

    # 以后就在这个方法里面自定义组件
    def createWidget(self):
        #         创建组件
        main_paned_window = PanedWindow(self, orient=HORIZONTAL, sashrelief=SUNKEN)  # 默认是左右分布的
        main_paned_window.pack(fill=BOTH, expand=1)

        left_paned_window = PanedWindow(main_paned_window, orient=VERTICAL, sashrelief=SUNKEN)
        main_paned_window.add(left_paned_window)

        self.industry_frame = Frame( left_paned_window )
        left_paned_window.add( self.industry_frame )
        self.query_industry_spot()

        self.plot_frame = Frame( left_paned_window )
        left_paned_window.add( self.plot_frame )
        Label(self.plot_frame, text='matplotlib').pack()

        right_paned_window = PanedWindow(main_paned_window, orient=VERTICAL, sashrelief=SUNKEN)
        main_paned_window.add(right_paned_window)
        self.cons_frame=Frame(right_paned_window)
        self.cons_frame.pack(fill=BOTH, expand=1)
        Label(self.cons_frame, text='index').pack()


    def query_industry_spot(self ):
        df_spot =IndustryData().get_index_spot()
        columns = df_spot.columns.tolist()
        print('columns', columns )
        self.tree = ttk.Treeview(self.industry_frame, show="headings", columns=columns, selectmode=BROWSE)
        self.tree.pack()
        VScrollX = ttk.Scrollbar(self.tree, orient='horizontal', command=self.tree.xview)
        VScrollY = ttk.Scrollbar(self.tree, orient='vertical', command=self.tree.yview)
        # 给treeview添加配置
        self.tree.configure(xscrollcommand=VScrollX.set)
        self.tree.configure(yscrollcommand=VScrollY.set)
        for col in columns:
            self.tree.column(col, anchor="center", width=20)
            # self.tree.heading(col, text=col)
            self.tree.column('#0', stretch=0)
            self.tree.heading(col, text=col, command=lambda _col=col: self.spot_treeview_sort(self.tree, _col, False))

        for rowIndex in df_spot.index:
            # print( df.loc[rowIndex].values )
            self.tree.insert('', rowIndex, values=tuple(df_spot.loc[rowIndex].values))
        print('-----------')
        self.tree.pack(expand=True, fill=BOTH)
        self.tree.bind('<<TreeviewSelect>>', self.spot_treeview_select)

    def query_index_cons(self, code):
        df_cons =IndustryData().get_index_cons(code)
        columns = df_cons.columns.tolist()
        print('columns', columns )
        for child in self.cons_frame.winfo_children():
            child.destroy()
        self.cons_tree = ttk.Treeview(self.cons_frame, show="headings", columns=columns, selectmode=BROWSE)
        self.cons_tree.pack()
        VScrollX = ttk.Scrollbar(self.cons_tree, orient='horizontal', command=self.cons_tree.xview)
        VScrollY = ttk.Scrollbar(self.cons_tree, orient='vertical', command=self.cons_tree.yview)
        # 给treeview添加配置
        self.cons_tree.configure(xscrollcommand=VScrollX.set)
        self.cons_tree.configure(yscrollcommand=VScrollY.set)
        for col in columns:
            self.cons_tree.column(col, anchor="center", width=20)
            # self.tree.heading(col, text=col)
            self.cons_tree.column('#0', stretch=0)
            self.cons_tree.heading(col, text=col, command=lambda _col=col: self.cons_treeview_sort(self.cons_tree, _col, False))

        for rowIndex in df_cons.index:
            # print( df.loc[rowIndex].values )
            self.cons_tree.insert('', rowIndex, values=tuple(df_cons.loc[rowIndex].values))
        print('-----------')
        self.cons_tree.pack(expand=True, fill=BOTH)
        self.cons_tree.bind('<<TreeviewSelect>>', self.cons_treeview_select)

    def query_index_daily(self, code):

        df = IndustryData().get_index_daily(code)
        print( df.head(10) )

        df['date']=df['date'].apply( lambda x:date2num(x))
        ohlc=df[['date','open','high','low','close']]
        ohlc.rename(columns={'date':'t'}, inplace=True)
        ohlc['open']=ohlc['open'].apply( lambda  x:float(x))
        ohlc['high']=ohlc['high'].apply( lambda  x:float(x))
        ohlc['low']=ohlc['low'].apply( lambda  x:float(x))
        ohlc['close']=ohlc['close'].apply( lambda  x:float(x))

        print( ohlc.head(10))
        self.figure = Figure(figsize=(5, 4), dpi=100)
        self.f_plot = self.figure.add_subplot(111)
        self.canvs = FigureCanvasTkAgg(self.figure, self)
        self.canvs.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


        self.f_plot.clear()
        self.f_plot.xaxis_date()
        self.f_plot.autoscale_view()
        plt.xticks(rotation=45)
        plt.yticks()
        plt.title(" {0}".format(code))
        plt.xlabel("date")
        plt.ylabel("price")
        print( ohlc.head(10))
        print( ohlc.values)
        mpf.candlestick_ohlc(self.f_plot, ohlc.values, colorup='red', colordown='green')
        #  画 10,20日均线
        plt.legend(loc='best', shadow=True)
        plt.grid()
        self.canvs.draw()
    # 鼠标选中一行回调
    def spot_treeview_select(self, event):
        # selfs = event.widget.selection()  # event.widget获取Treeview对象，调用selection获取选择对象名称
        tree = event.widget  # event.widget获取Treeview对象，调用selection获取选择对象名称
        for item in tree.selection():
            item_text = tree.item(item, "values")
            print(item_text[0], item_text)
            # self.matframe.draw_matplotlib(item_text[0])
            self.query_index_cons(item_text[0])
            self.query_index_daily( item_text[0])

    # 选中行
    def spot_treeview_sort(self,treeview, col, reverse):  # Treeview、列名、排列方式
        # set(item, column=None, value=None)
        # 指定item，如果不设定column和value，则返回他们的字典，如果设定了column，则返回该column的value，如果value也设定了，则作相应更改。
        # get_children(item=None)
        # 返回一个item的所有子item，这个子item是一个列表形式，如果item没指定，则返回根目录的item
        l = [(treeview.set(k, col), k) for k in treeview.get_children('')]
        print(treeview.get_children(''))
        try:
            l.sort(key=lambda t: float(t[0]), reverse=reverse)
        except ValueError:
            l.sort(reverse=reverse)
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            treeview.move(k, '', index)
            print(k)
        treeview.heading(col, command=lambda: self.spot_treeview_sort(treeview, col, not reverse))  # 重写标题，使之成为再点倒序的标题
    # 鼠标选中一行回调

    def cons_treeview_select(self, event):
        # selfs = event.widget.selection()  # event.widget获取Treeview对象，调用selection获取选择对象名称
        tree = event.widget  # event.widget获取Treeview对象，调用selection获取选择对象名称
        for item in tree.selection():
            item_text = tree.item(item, "values")
            print(item_text[0], item_text)
            # self.matframe.draw_matplotlib(item_text[0])

    # 选中行
    def cons_treeview_sort(self,treeview, col, reverse):  # Treeview、列名、排列方式
        # set(item, column=None, value=None)
        # 指定item，如果不设定column和value，则返回他们的字典，如果设定了column，则返回该column的value，如果value也设定了，则作相应更改。
        # get_children(item=None)
        # 返回一个item的所有子item，这个子item是一个列表形式，如果item没指定，则返回根目录的item
        l = [(treeview.set(k, col), k) for k in treeview.get_children('')]
        print(treeview.get_children(''))
        try:
            l.sort(key=lambda t: float(t[0]), reverse=reverse)
        except ValueError:
            l.sort(reverse=reverse)
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            treeview.move(k, '', index)
            print(k)
        treeview.heading(col, command=lambda: self.spot_treeview_sort(treeview, col, not reverse))  # 重写标题，使之成为再点倒序的标题

if __name__ == '__main__':
    root = Tk()
    root.title('数学曲线窗口')
    root.geometry('320x320+200+200')
    industry_frame = IndustryFrame( root )
    industry_frame.pack(fill=BOTH, expand=1)
    root.mainloop()