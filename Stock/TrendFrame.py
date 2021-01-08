
import  tkinter as tk
from tkinter import  *

class TrendFrame(Frame ):
    def __init__(self, root=None):
        super().__init__(root)  # 调用父类的初始化方法
        self.root = root
        self.create_paned_window(self.root)


    def create_paned_window(self, root):
        self.lable=Label(self, text='trend')
        self.lable.pack(side=TOP)
        self.frame = Frame(self)
        self.frame.pack(fill=BOTH, expand=1)


