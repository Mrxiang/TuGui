from Stock.Utils import  *
from Stock.MatFrame import  *
from tkinter import  ttk
import  pandas as pd
from tkinter import  *

from Stock.ReportData import  *


class ReportMainFrame(Frame ):
    def __init__(self, root=None):
        super().__init__(root)  # 调用父类的初始化方法
        self.root = root
        self.create_paned_window()


    def create_paned_window(self):
        main_paned_window = PanedWindow(self, orient=VERTICAL, sashrelief=SUNKEN)  # 默认是左右分布的
        main_paned_window.pack(fill=BOTH, expand=1)

        top_paned_window = PanedWindow(main_paned_window, orient=HORIZONTAL, sashrelief=SUNKEN)
        main_paned_window.add(top_paned_window)

        self.data_frame = Frame( top_paned_window )
        self.data_frame.pack(fill=BOTH, expand=1)
        title_frame = Frame( self.data_frame )
        title_frame.pack(fill=BOTH, expand=1)

        yvalue = tk.StringVar()  # 窗体自带的文本，新建一个值
        year_box = ttk.Combobox(title_frame, textvariable=yvalue, state='readonly')  # 初始化
        ylist = list(np.arange(2020, 1990, -1))
        year_box["values"] = list(ylist)
        year_box.pack(side=tk.LEFT)
        year_box.current(0)  # 选择第一个

        qvalue = tk.StringVar()  # 窗体自带的文本，新建一个值
        quarter_box = ttk.Combobox(title_frame, textvariable=qvalue, state='readonly')  # 初始化
        qlist = np.arange(1, 5)
        quarter_box["values"] = list(qlist)
        quarter_box.pack(side=tk.LEFT)
        quarter_box.current(0)  # 选择第一个

        query = Button(title_frame, text='查询', command = lambda :self.query_report( yvalue.get(), qvalue.get()))
        query.pack(side=LEFT)

        self.query_current_report()

        bottom_paned_window = PanedWindow(main_paned_window, orient=HORIZONTAL, sashrelief=SUNKEN)
        main_paned_window.add(bottom_paned_window)

        self.bottom_left_window= Frame( bottom_paned_window )
        bottom_paned_window.add( self.bottom_left_window )
        # self.kframe = KFrame(bottom_paned_window, code='000333')
        self.matframe = MatFrame(self.bottom_left_window)
        self.matframe.pack()

        self.bottom_right_window = Frame(bottom_paned_window)
        bottom_paned_window.add( self.bottom_right_window)
        self.notice_lable = Label(self.bottom_right_window, text='Message')
        self.notice_lable.pack(fill=X)


    def query_current_report(self ):
        today = datetime.date.today()
        year = today.year
        quarter = (today.month - 1) // 3 + 1
        print( year, quarter , type(year),  type(quarter))
        try:
            df = ReportData().get_forecast_and_report( year,  quarter)
            columns = df.columns.tolist()
        except:
            # columns = tuple(ReportDataUtils.keys())
            columns = tuple(ForecastReportDataUtils.keys())
            df =pd.DataFrame(columns=columns)

        print("----")
        print('columns', columns )
        self.tree = ttk.Treeview(self.data_frame, show="headings", columns=columns, selectmode=tk.BROWSE)
        self.tree.pack()
        """
            定义滚动条控件
        """
        VScrollX = ttk.Scrollbar(self.tree, orient='horizontal', command=self.tree.xview)
        VScrollY = ttk.Scrollbar(self.tree, orient='vertical', command=self.tree.yview)

        # 给treeview添加配置
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
            self.tree.column('#0', stretch=0)
            self.tree.heading(col, text=ForecastReportDataUtils.get(col), command=lambda _col=col: self.treeview_sort_column(self.tree, _col, False))

        for rowIndex in df.index:
            # print( df.loc[rowIndex].values )
            self.tree.insert('', rowIndex, values=tuple(df.loc[rowIndex].values))
        print('-----------')

        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree.bind('<ButtonRelease-1>', self.treeview_click)
        self.tree.bind('<<TreeviewSelect>>', self.treeview_select)

    def query_report(self, year, quart):
        df = ReportData().get_forecast_and_report(year, quart)
        columns = df.columns.tolist()
        """
            定义滚动条控件
            orient为滚动条的方向，vertical--纵向，horizontal--横向
            command=self.tree.yview 将滚动条绑定到treeview控件的Y轴
        """
        VScrollX = ttk.Scrollbar(self.tree, orient='horizontal', command=self.tree.xview)
        VScrollY = ttk.Scrollbar(self.tree, orient='vertical', command=self.tree.yview)
        # VScrollY.place(relx=0.971, rely=0.028, relwidth=0.024, relheight=0.958)
        VScrollX.pack(fill=X, side=BOTTOM)
        VScrollY.pack(fill=Y, side=RIGHT)

        # 给treeview添加配置
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
            self.tree.column(col, anchor="center")
            self.tree.column('#0', stretch=0)
            self.tree.heading(col, text=ForecastReportDataUtils.get(col), command=lambda _col=col: self.treeview_sort_column(self.tree, _col, False))

        for rowIndex in df.index:
            self.tree.insert('', rowIndex, values=tuple(df.loc[rowIndex].values))
        print('-----------')
        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree.bind('<ButtonRelease-1>', self.treeview_click)
        self.tree.bind('<<TreeviewSelect>>', self.treeview_select)
    # 获取当前点击行的值
    def treeview_click(self,event):  # 单击
        # selfs = event.widget.selection()  # event.widget获取Treeview对象，调用selection获取选择对象名称
        tree = event.widget  # event.widget获取Treeview对象，调用selection获取选择对象名称
        for item in tree.selection():
            item_text = tree.item(item, "values")
            print(item_text)

    # 鼠标左键抬起

    # 鼠标选中一行回调
    def treeview_select(self, event):
        # selfs = event.widget.selection()  # event.widget获取Treeview对象，调用selection获取选择对象名称
        tree = event.widget  # event.widget获取Treeview对象，调用selection获取选择对象名称
        for item in tree.selection():
            item_text = tree.item(item, "values")
            print(item_text)
            self.matframe.draw_matplotlib(item_text[0])

    # 选中行
    def treeview_sort_column(self,treeview, col, reverse):  # Treeview、列名、排列方式
        # set(item, column=None, value=None)
        # 指定item，如果不设定column和value，则返回他们的字典，如果设定了column，则返回该column的value，如果value也设定了，则作相应更改。
        # get_children(item=None)
        # 返回一个item的所有子item，这个子item是一个列表形式，如果item没指定，则返回根目录的item
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


    def start_progress(self):
        self.pb.start()


if __name__ == '__main__':
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
    window.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
    # 设置窗口图标
    # window.iconbitmap("./image/android_icon.ico")
    # 设置窗口宽高固定
    window.resizable(True, True)
    reportframe = ReportMainFrame(window)
    reportframe.pack(fill=BOTH, expand=1)
    mainloop()