import tkinter as tk
from tkinter import  *
from Utils import  *
from KFrame import  *
from MatFrame import  *
from tkinter import  ttk
class HomeFrame(Frame ):
    def __init__(self, root=None):
        super().__init__(root)  # 调用父类的初始化方法
        self.root = root