import tushare as ts

class Token():
    def __init__(self):
        super().__init__()  # 调用父类的初始化方法
        self.pro = ts.pro_api('***********')
