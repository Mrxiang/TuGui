from Home import Utils
from Home.HomeData import HomeData
from Home.Utils import HomeDataUtils
from Home.Watch import Watch
from Stock.MatFrame import  *
from tkinter import messagebox
from tkinter import  ttk
import threading
from concurrent.futures import ThreadPoolExecutor

class HomeFrame(Frame ):
    def __init__(self, master=None):  # 参数  源码就是这样写，master代表的是父容器
        # Frame是父类，得主动的调用父类 的构造器
        super().__init__(master)  # super() 代表的是父类的定义，而不是父类的对象
        self.master = master
        # self.pack()  #这个组件的定位
        self.createWidget()  # 自定义方法，在这个方法里自定义组件
        global timer
        timer = threading.Timer(60.0, self.get_data_from_threadPool, [])
        timer.start()
        global  threadPool
        threadPool = ThreadPoolExecutor(max_workers=4, thread_name_prefix="home_")
    # 以后就在这个方法里面自定义组件
    def createWidget(self):
        #         创建组件
        # self.timestr = StringVar()
        # label = Label(self, textvariable = self.timestr)
        # label.pack()
        # current =datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # self.timestr1.set(current)
        watch = Watch(self)
        watch.start()
        df= HomeData().get_today_all( )
        print(df)
        columns = df.columns.tolist()

        self.tree = ttk.Treeview(self, show="headings", columns=columns, selectmode='browse')
        self.tree.pack()
        """
            定义滚动条控件
        """
        VScrollX = ttk.Scrollbar(self.tree, orient='horizontal', command=self.tree.xview)
        VScrollY = ttk.Scrollbar(self.tree, orient='vertical', command=self.tree.yview)
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
            # self.tree.column('#0', stretch=0)
            self.tree.heading(col, text=HomeDataUtils.get(col), command=lambda _col=col: self.treeview_sort_column(self.tree, _col, False))
            # self.tree.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(self.tree, _col, False))

        for rowIndex in df.index:
            # print( df.loc[rowIndex].values )
            self.tree.insert('', rowIndex, values=tuple(df.loc[rowIndex].values))
        print('-----------')

        self.tree.pack(expand=True, fill='both')
    def updateWidget(self, df):
        items = self.tree.get_children()
        [self.tree.delete(item) for item in items]
        for rowIndex in df.index:
            # print( df.loc[rowIndex].values )
            self.tree.insert('', rowIndex, values=tuple(df.loc[rowIndex].values))

    def get_data_from_threadPool(self ):

        future = threadPool.submit(self.get_today_all_data )
        # future.add_done_callback(test_result)
        print('future',future.result())
        df = future.result()
        self.updateWidget( df)

        timer = threading.Timer(60.0, self.get_data_from_threadPool, [])
        timer.start()
    def get_today_all_data(self):
        df = HomeData().get_today_all()
        return  df

    def __del__(self):
        # timer.s
        pass
if __name__ == '__main__':
    root = Tk()
    root.title('数学曲线窗口')
    root.geometry('320x320+200+200')
    homeframe  =HomeFrame( root)
    homeframe.pack(fill=BOTH, expand=1)
    root.mainloop()