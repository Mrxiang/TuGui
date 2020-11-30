import  tkinter as tk
from tkinter import  *
from  ReportDataFrame import  *

def create_menu(root ):
    menubar = tk.Menu(root)
    filemenu = tk.Menu(menubar, tearoff=0)
    # 将上面定义的空菜单命名为File，放在菜单栏中，就是装入那个容器中
    menubar.add_cascade(label='File', menu=filemenu)

    # 在File中加入New、Open、Save等小菜单，即我们平时看到的下拉菜单，每一个小菜单对应命令操作。
    filemenu.add_command(label='New')
    filemenu.add_command(label='Open')
    filemenu.add_command(label='Save')
    filemenu.add_separator()  # 添加一条分隔线
    filemenu.add_command(label='Exit', command=quit)  # 用tkinter里面自带的quit()函数
    root.config( menu=menubar )

def main():
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
    window.title("火器时代")
    # 设置窗口初始位置在屏幕居中
    window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
    # 设置窗口图标
    # window.iconbitmap("./image/android_icon.ico")
    # 设置窗口宽高固定
    window.resizable(True,True )
    #增加菜单
    create_menu( window )
    #增加数据分析窗口

    report_data_frame = ReportDataFrame( window  )
    report_data_frame.pack()

    window.mainloop()


if __name__ == '__main__':
    main()