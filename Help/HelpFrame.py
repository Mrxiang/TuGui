from tkinter import  *
from tkinter import messagebox
import tkinter as tk
from tkinter import scrolledtext

class HelpFrame(Frame): #自己创建的这个类就是一个组件，这个要继承Frame类

    def __init__(self, master=None):  # 参数  源码就是这样写，master代表的是父容器
        # Frame是父类，得主动的调用父类 的构造器
        super().__init__(master)  # super() 代表的是父类的定义，而不是父类的对象
        self.master = master
        # self.pack()  #这个组件的定位
        self.createWidget()  # 自定义方法，在这个方法里自定义组件

    # 以后就在这个方法里面自定义组件
    def createWidget(self):
        #         创建组件
        label = Label( self, text='数据来源'+'https://www.waditu.com/')
        label.pack()
        scr = scrolledtext.ScrolledText(self, font=("隶书", 18))  # 滚动文本框（宽，高（这里的高应该是以行数为单位），字体样式）
        scr.pack()
        # scr.insert(tk.END, '数据来源'+'https://www.waditu.com/'+"\n")



if __name__ == '__main__':
    root = Tk()
    root.title('数学曲线窗口')
    root.geometry('320x320+200+200')
    helpframe = HelpFrame( root )
    helpframe.pack()
    root.mainloop()