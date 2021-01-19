
import  tkinter as tk
from concurrent.futures.thread import ThreadPoolExecutor
from tkinter import  *
from tkinter import ttk
import pandas as pd
import numpy as np
from Stock.TrendData import TrendData


class TrendFrame(Frame ):
    def __init__(self, root=None):
        super().__init__(root)  # 调用父类的初始化方法
        self.root = root
        self.create_paned_window()


    def create_paned_window(self):

        df =TrendData().get_trend_data()
        columns = df.columns.tolist()


        main_paned_window = PanedWindow(self, orient=VERTICAL, sashrelief=SUNKEN)  # 默认是左右分布的
        main_paned_window.pack(fill=BOTH, expand=1)

        top_paned_window = PanedWindow(main_paned_window, orient=HORIZONTAL, sashrelief=SUNKEN)
        main_paned_window.add(top_paned_window)

        self.data_frame = Frame( top_paned_window )
        self.data_frame.pack(fill=BOTH, expand=1)
        title_frame = Frame( self.data_frame )
        yvalue = tk.StringVar()  # 窗体自带的文本，新建一个值
        year_box = ttk.Combobox(title_frame, textvariable=yvalue, state='readonly')  # 初始化
        ylist = list(np.arange(2020, 1990, -1))
        year_box["values"] = list(ylist)
        year_box.pack(side=tk.LEFT)
        year_box.current(0)  # 选择第一个

        qvalue = tk.StringVar()  # 窗体自带的文本，新建一个值
        quarter_box = ttk.Combobox(title_frame, textvariable=qvalue, state='readonly')  # 初始化
        qlist = np.arange(1, 5)
        quarter_box["values"] = list(qlist)
        quarter_box.pack(side=tk.LEFT)
        quarter_box.current(0)  # 选择第一个

        query = Button(title_frame, text='查询', command = lambda :self.query_report( yvalue.get(), qvalue.get()))
        query.pack(side=LEFT)
        title_frame.pack()

        #self.daily_frame = Frame( top_paned_window )
        self.tree = ttk.Treeview(self.data_frame, show="headings", columns=columns, selectmode='browse')
        self.tree.pack()
        """
            定义滚动条控件
        """
        VScrollX = ttk.Scrollbar(self.tree, orient='horizontal', command=self.tree.xview)
        VScrollY = ttk.Scrollbar(self.tree, orient='vertical', command=self.tree.yview)

        self.tree.configure(xscrollcommand=VScrollX.set)
        self.tree.configure(yscrollcommand=VScrollY.set)
        for col in columns:
            self.tree.column(col, anchor="center", width=20)
            # self.tree.heading(col, text=col)
            self.tree.column('#0', stretch=0)
            self.tree.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(self.tree, _col, False))

        for rowIndex in df.index:
            # print( df.loc[rowIndex].values )
            self.tree.insert('', rowIndex, values=tuple(df.loc[rowIndex].values))
        print('-----------')

        self.tree.pack(expand=True, fill='both')

        bottom_paned_window = PanedWindow(main_paned_window, orient=HORIZONTAL, sashrelief=SUNKEN)
        main_paned_window.add(bottom_paned_window)

    def treeview_sort_column(self,treeview, col, reverse):  # Treeview、列名、排列方式
        l = [(treeview.set(k, col), k) for k in treeview.get_children('')]
        print(treeview.get_children(''))
        try:
            l.sort(key=lambda t: float(t[0]), reverse=reverse)
        except ValueError:
            l.sort(reverse=reverse)
        # rearrange items in sorted positions
        for index, (val, k) in enumerate(l):  # 根据排序后索引移动
            treeview.move(k, '', index)
            print(k)
        treeview.heading(col, command=lambda: self.treeview_sort_column(treeview, col, not reverse))  # 重写标题，使之成为再点倒序的标题

if __name__ == '__main__':
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()
    # 设置窗口大小
    winWidth = window.winfo_screenwidth()
    winHeight = window.winfo_screenheight()
    # 获取屏幕分辨率
    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()

    x = int((screenWidth - winWidth) / 2)
    y = int((screenHeight - winHeight) / 2)
    # 设置主窗口标题
    window.title("像机构一样思考")
    # 设置窗口初始位置在屏幕居中
    # window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
    window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
    # 设置窗口图标
    # window.iconbitmap("./image/android_icon.ico")
    # 设置窗口宽高固定
    window.resizable(True, True)
    trendframe = TrendFrame(window)
    trendframe.pack(fill=BOTH, expand=1)
    window.mainloop()