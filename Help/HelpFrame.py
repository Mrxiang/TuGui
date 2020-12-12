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
    window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
    # 设置窗口图标
    # window.iconbitmap("./image/android_icon.ico")
    # 设置窗口宽高固定
    window.resizable(True, True)
    helpframe = HelpFrame(window)
    helpframe.pack()
    mainloop()