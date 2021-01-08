# 显示手柄和分割线
from Fund.FundFrame import FundFrame
from Help.HelpFrame import HelpFrame
from Home.HomeFrame import HomeFrame
from Industry.IndustryFrameL1 import IndustryFrameL1
from Industry.IndustryFrameL3 import IndustryFrameL3
from Macro.MacroFrame import MacroFrame
from Stock.ReportMainFrame import  *
from ConvertibleBond.CBFrame import   *
from MainFrame import  *
from tkinter import messagebox
from New.NewMessage import SplashMessage

# pd.options.display.max_columns = None
# pd.options.display.max_rows = None
from Stock.TrendFrame import TrendFrame


def create_menu( root ):
    # 第5步，创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
    menubar = tk.Menu(root)
    # 第6步，创建一个File菜单项（默认不下拉，下拉内容包括New，Open，Save，Exit功能项）
    industry_menu = tk.Menu(menubar, tearoff=0)
    stock_menu = tk.Menu(menubar, tearoff=0)
    # 主页
    menubar.add_command(label='主页', command=add_home_frame)
    # 宏观经济
    menubar.add_command(label='宏观经济', command=add_mecro_frame)
    # 行业分析
    menubar.add_cascade(label='行业分析', menu=industry_menu)
    industry_menu.add_command(label='申万一级行业分析', command=add_L1_industry_frame)
    industry_menu.add_command(label='申万三级行业分析', command=add_L3_industry_frame)
    # 个股策略
    menubar.add_cascade(label='个股策略', menu=stock_menu)
    stock_menu.add_command(label='业绩报表', command=add_report_frame)
    stock_menu.add_command(label='业绩报表vip', command=quit)
    stock_menu.add_command(label='趋势复盘', command=add_trend_frame)
    stock_menu.add_command(label='Save', command=quit)
    stock_menu.add_command(label='Exit', command=quit)  # 用tkinter里面自带的quit()函数
    # 可转债
    menubar.add_command(label='可转债', command=add_convertible_bonds_frame)
    # 公募基金
    menubar.add_command(label='公募基金', command=add_fund_frame)
    # 帮助
    menubar.add_command(label='帮助', command=add_help_frame)
    # 第11步，创建菜单栏完成后，配置让菜单栏menubar显示出来
    root.config(menu=menubar)


def add_home_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    homeframe = HomeFrame(mainframe)
    homeframe.pack(fill=BOTH, expand=1)

def add_report_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    reportframe = ReportMainFrame(mainframe)
    reportframe.pack(fill=BOTH, expand=1)

def add_trend_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    trendframe = TrendFrame(mainframe)
    trendframe.pack(fill=BOTH, expand=1)

def add_L1_industry_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    application = IndustryFrameL1(mainframe)
    application.pack(fill=BOTH, expand=1)

def add_L3_industry_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    application = IndustryFrameL3(mainframe)
    application.pack(fill=BOTH, expand=1)
def add_convertible_bonds_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    application = CBFrame(mainframe)
    application.pack(fill=BOTH, expand=1)

def add_fund_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    application = FundFrame(mainframe)
    application.pack(fill=BOTH, expand=1)

def add_mecro_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    application = MacroFrame(mainframe)
    application.pack(fill=BOTH, expand=1)

def add_help_frame():
    for widget in mainframe.winfo_children():
        widget.destroy()
    application = HelpFrame(mainframe)
    application.pack(fill=BOTH, expand=1)
def main():
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
    window.geometry('640x480+200+200')
    # 设置窗口图标
    # window.iconbitmap("./image/android_icon.ico")
    # 设置窗口宽高固定
    window.resizable(True, True)

    global mainframe
    mainframe = MainFrame( window )
    mainframe.pack(fill=BOTH, expand=1)

    create_menu( window )

    message = SplashMessage()
    message.title('新股')
    message.geometry('480x320+200+200')
    message.attributes("-topmost", True)  # 永远处于顶层
    message.mainloop()

    window.mainloop()
    # 分割线上的类似正方形的东西就是handle

if __name__ == '__main__':
    main()