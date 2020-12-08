from PerformReport.Utils import  *
from PerformReport.MatFrame import  *
from tkinter import  ttk
import  pandas as pd

class ReportMainFrame(Frame ):
    def __init__(self, root=None):
        super().__init__(root)  # 调用父类的初始化方法
        self.root = root
        self.create_paned_window(self.root)


    def create_paned_window(self, root):
        main_paned_window = PanedWindow(root, orient=VERTICAL, sashrelief=SUNKEN)  # 默认是左右分布的
        main_paned_window.pack(fill=BOTH, expand=1)

        top_paned_window = PanedWindow(main_paned_window, orient=HORIZONTAL, sashrelief=SUNKEN)
        main_paned_window.add(top_paned_window)

        # data_frame = ReportDataFrame(top_paned_window)
        # top_paned_window.add(data_frame)
        self.data_frame = Frame( top_paned_window )
        title_frame = Frame( self.data_frame )

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

        query = Button(title_frame, text='查询', command = lambda :self.query_report( yvalue, qvalue))
        query.pack(side=LEFT)

        # self.pb = ttk.Progressbar(title_frame, length=400, value=0, mode="determinate")
        # self.pb.pack(pady=10)
        # startbtn = Button(title_frame, text="开始", command=lambda :root.start_progress(self))
        # startbtn.pack()
        title_frame.pack()
        # load current report
        self.query_current_report()
        top_paned_window.add(self.data_frame)

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
            df = ts.get_report_data( year,  quarter)
            df = df.drop_duplicates(['code'], keep='first')
            sub_df = df[['eps', 'eps_yoy', 'bvps', 'roe', 'epcf', 'net_profits', 'profits_yoy']]
            sub_df.fillna(0)
            df[['eps', 'eps_yoy', 'bvps', 'roe', 'epcf', 'net_profits', 'profits_yoy']] = sub_df
            print("----")
            print(df)
            columns = df.columns.tolist()

        except:
            columns = tuple(ReportDataUtils.keys())
            df =pd.DataFrame(columns=columns)

        print("----")
        print('columns', columns )
        self.tree = ttk.Treeview(self.data_frame, show="headings", columns=columns, selectmode=tk.BROWSE)
        self.tree.pack()
        """
            定义滚动条控件
            orient为滚动条的方向，vertical--纵向，horizontal--横向
            command=self.tree.yview 将滚动条绑定到treeview控件的Y轴
        """
        VScrollX = ttk.Scrollbar(self.tree, orient='horizontal', command=self.tree.xview)
        VScrollY = ttk.Scrollbar(self.tree, orient='vertical', command=self.tree.yview)
        # VScrollX.pack(fill=X, side=BOTTOM)
        # VScrollY.pack(fill=Y, side=RIGHT)

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
            self.tree.heading(col, text=col)
            self.tree.column('#0', stretch=0)
            self.tree.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(self.tree, _col, False))

        print('-----------')
        for rowIndex in df.index:
            # print( df.loc[rowIndex].values )
            self.tree.insert('', rowIndex, values=tuple(df.loc[rowIndex].values))
        print('-----------')

        self.tree.pack(expand=True, fill=tk.BOTH)
        self.tree.bind('<ButtonRelease-1>', self.treeview_click)
        self.tree.bind('<<TreeviewSelect>>', self.treeview_select)

    def query_report(self, year, quart):
        print(year.get(), quart.get())
        df = ts.get_report_data( int(year.get()),  int(quart.get()))
        df = df.drop_duplicates(['code'], keep='first')
        sub_df = df[['eps', 'eps_yoy', 'bvps', 'roe', 'epcf', 'net_profits', 'profits_yoy']]
        sub_df.fillna(0)
        df[['eps', 'eps_yoy', 'bvps', 'roe', 'epcf', 'net_profits', 'profits_yoy']] = sub_df
        print("----")
        print(df)
        print("----")
        columns = df.columns.tolist()
        # self.tree = ttk.Treeview(self, show="headings", columns=columns, selectmode=tk.BROWSE)
        # self.tree.pack(side=BOTTOM)
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
            self.tree.heading(col, text=col)
            self.tree.column('#0', stretch=0)
            self.tree.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(self.tree, _col, False))

        print('-----------')
        for rowIndex in df.index:
            # print( df.loc[rowIndex].values )
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