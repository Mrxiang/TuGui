from tkinter import *
import  tkinter as tk
from MatFrame import  *
from KFrame import  *
from ReportMainFrame import  *
from MainFrame import  *
from HomeFrame import  *
from tkinter import messagebox

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
        self.btn = Button(self)
        self.btn["text"] = "点击送花"
        self.btn.pack()
        self.btn["command"] = self.songhua
#         创建一个退出按钮
        self.btnquit = Button(self,text = "退出",command = quit)
        self.btnquit.pack()
    def songhua(self):
        messagebox.showinfo("送花","送很多的花")

def create_menu( root ):
    # 第5步，创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
    menubar = tk.Menu(root)
    # 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
    stockmenu = tk.Menu(menubar, tearoff=0)
    menubar.add_command(label='主页', command=add_home_frame)
    menubar.add_cascade(label='个股策略', menu=stockmenu)
    # 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
    stockmenu.add_command(label='业绩报表', command=add_report_frame)
    stockmenu.add_command(label='Open', command=quit)
    stockmenu.add_command(label='Save', command=quit)
    stockmenu.add_command(label='Exit', command=quit)  # 用tkinter里面自带的quit()函数
    menubar.add_command(label='行业分析', command=add_industry_frame)
    menubar.add_command(label='宏观经济', command=add_mecro_frame)
    # 第11步，创建菜单栏完成后，配置让菜单栏menubar显示出来
    root.config(menu=menubar)


def add_home_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    homeframe = HomeFrame(mainframe)
    homeframe.pack()

def add_report_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    reportframe = ReportMainFrame(mainframe)
    reportframe.pack()

def add_industry_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    application = Application(mainframe)
    application.pack()

def add_mecro_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    application = Application(mainframe)
    application.pack()

def main():
    # 第1步，实例化object，建立窗口window
    window = tk.Tk()

    # 第2步，给窗口的可视化起名字
    window.title('My Window')
    # 第3步，设定窗口的大小(长 * 宽)
    window.geometry('500x300')  # 这里的乘是小x
    create_menu( window )
    global mainframe
    mainframe = MainFrame( window )
    mainframe.pack()
    mainloop()
    # 分割线上的类似正方形的东西就是handle

if __name__ == '__main__':
    main()