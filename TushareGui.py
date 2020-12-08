# 显示手柄和分割线
from Fund.FundFrame import FundFrame
from Help.HelpFrame import HelpFrame
from Home.HomeFrame import HomeFrame
from Industry.IndustryFrame import IndustryFrame
from Macro.MacroFrame import MacroFrame
from PerformReport.ReportMainFrame import  *
from ConvertibleBond.CBFrame import   *
from MainFrame import  *
from tkinter import messagebox


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
    menubar.add_command(label='可转债', command=add_convertible_bonds_frame)
    menubar.add_command(label='公募基金', command=add_fund_frame)
    menubar.add_command(label='宏观经济', command=add_mecro_frame)
    menubar.add_command(label='帮助', command=add_help_frame)
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
    application = IndustryFrame(mainframe)
    application.pack()

def add_convertible_bonds_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    application = CBFrame(mainframe)
    application.pack()

def add_fund_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    application = FundFrame(mainframe)
    application.pack()

def add_mecro_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    application = MacroFrame(mainframe)
    application.pack()

def add_help_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    application = HelpFrame(mainframe)
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