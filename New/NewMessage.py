import random
import tkinter as tk
import threading
from tkinter import  *
import tkinter as tk
from tkinter import ttk

from New import Utils
from New.NewData import NewData


class SplashMessage(tk.Tk):

    def __init__(self):
        super().__init__()

        self.create_widget()

    def create_widget(self):
        df= NewData().get_new_share()
        print(df)
        columns = df.columns.tolist()

        self.tree = ttk.Treeview(self, show="headings", columns=columns, selectmode='browse')
        self.tree.pack(fill=BOTH, expand=1)
        """
            定义滚动条控件
        """
        VScrollX = ttk.Scrollbar(self.tree, orient='horizontal', command=self.tree.xview)
        VScrollY = ttk.Scrollbar(self.tree, orient='vertical', command=self.tree.yview)
        self.tree.configure(xscrollcommand=VScrollX.set)
        self.tree.configure(yscrollcommand=VScrollY.set)
        # 设置表格文字居中
        # column(column, option=None, **kw)给各列设置属性，或返回属性。
        # 第一个column是列标识符.
        # 第二个option，如果不设置则返回所有属性的字典，如果设置则返回那个属性的值。kw里的option有5个
        # id：只读属性，返回列名。
        # anchor：文字在cell里的对齐方式，标准的tk的anchor属性
        # minwidth: 值，单位是像素，列的最小宽度
        # stretch: 布尔值，表示列的宽度是否随整个部件的改动而变化。
        # width：列宽，单位是像素。
        # 提示：如果要设置树状结构那列，用column=“#0”
        for col in columns:
            self.tree.column(col, anchor="center", width=20)
            # self.tree.heading(col, text=col)
            # self.tree.column('#0', stretch=0)
            self.tree.heading(col, text=Utils.NewDataUtils.get(col), command=lambda _col=col: self.treeview_sort_column(self.tree, _col, False))
            # self.tree.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(self.tree, _col, False))

        for rowIndex in df.index:
            # print( df.loc[rowIndex].values )
            self.tree.insert('', rowIndex, values=tuple(df.loc[rowIndex].values))
        print('-----------')

if __name__ == '__main__':
    win =  tk.Tk()
    win.title('新股申购')
    win.geometry('480x320+200+200')
    app = SplashMessage()
    app.title('窗口')
    app.geometry('320x320+200+200')
    app.attributes("-topmost", True)  # 永远处于顶层
    app.mainloop()
    win.mainloop()