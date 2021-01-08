
import  tushare as ts


class FundData():
    def __init__(self):
        pass
    def get_fund_data(self ):
        pro = ts.pro_api('ac147953b15f6ee963c164fc8ee8ef5228e58b75e5953ba5997ef117')

        df = pro.fund_basic(market='E')
        return  df



if __name__ == '__main__':

    df = FundData.get_fund_data()
    print( df )

