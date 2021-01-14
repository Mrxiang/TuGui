

import  tkinter as tk
from concurrent.futures.thread import ThreadPoolExecutor
from tkinter import  *
from tkinter import ttk
import pandas as pd

from Stock.HKData import HKData


class HKFrame(Frame ):
    def __init__(self, root=None):
        super().__init__(root)  # 调用父类的初始化方法
        self.root = root
        self.create_paned_window()


    def create_paned_window(self):

        df =HKData().get_hk_data()
        columns = df.columns.tolist()

        main_paned_window = PanedWindow(self, orient=VERTICAL, sashrelief=SUNKEN)  # 默认是左右分布的
        main_paned_window.pack(fill=BOTH, expand=1)

        top_paned_window = PanedWindow(main_paned_window, orient=HORIZONTAL, sashrelief=SUNKEN)
        main_paned_window.add(top_paned_window)
        self.daily_frame = Frame( top_paned_window )
        self.daily_frame.pack(fill=BOTH, expand=1)
        self.tree = ttk.Treeview(self.daily_frame, show="headings", columns=columns, selectmode='browse')
        self.tree.pack(expand=True, fill=tk.BOTH)

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
        self.fin_frame = Frame( bottom_paned_window )
        self.fin_frame.pack(expand=True, fill='both')
        self.label=Label(self.fin_frame, text='finance')
        self.label.pack()

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
    root = Tk()
    root.title('数学曲线窗口')
    root.geometry('320x320+200+200')
    hkframe = HKFrame(root)
    hkframe.pack(fill=BOTH, expand=1)
    root.mainloop()