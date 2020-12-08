
import tushare as ts
import  pandas as pd
import datetime
import numpy as np
from sqlalchemy import create_engine

def get_forecast_and_report_backtesting( year , quarter ):
        df_forecast = ts.forecast_data(year, quarter)
        df_forecast.drop_duplicates('code', keep='first')
        print('forecast', df_forecast.shape, df_forecast.columns )
        df_forecast.drop(['name'], axis=1, inplace=True)
        print( 'forecast',df_forecast.shape, df_forecast.columns)

        df_report = ts.get_report_data(year, quarter)
        df_report.drop_duplicates('code', keep='first')
        print('report', df_report.shape, df_report.columns)
        df_report['report_date']= df_report['report_date'].apply(lambda x: str(year)+'-'+x)
        print('report', df_report.shape, df_report.columns)



        df_forecast_report= pd.merge( df_report, df_forecast, on='code', how='left')
        print('forecast_report', df_forecast_report.shape, df_forecast_report.columns )

        df_forecast_report['forecast_close']=None
        df_forecast_report['report_close']=None
        df_forecast_report['close_5']=None
        df_forecast_report['close_10']=None
        df_forecast_report['close_15']=None
        df_forecast_report['close_30']=None
        df_forecast_report['close_60']=None
        df_forecast_report['close_90']=None
        print( df_forecast_report.shape)
        df_forecast_report = df_forecast_report.head(10)
        #
        for index, row in df_forecast_report.iterrows():
                print( '%d / %d'%(index, df_forecast_report.shape[0]), row )
                code =row.code
                # 取预告日收盘价
                if isinstance(row.report_date_y, str) :
                        forecast_date= datetime.datetime.strptime( row.report_date_y, '%Y-%m-%d').date()
                        forecast_hist=ts.get_hist_data( code, forecast_date.strftime('%Y-%m-%d'), forecast_date.strftime('%Y-%m-%d'))
                        print(code,'获取预告日价格')
                        if forecast_hist.shape[0] >0 :
                                row['forecast_close']=forecast_hist['close'].mean()
                # 取报告日收盘价
                if isinstance( row.report_date_x, str):
                        report_date = datetime.datetime.strptime(row.report_date_x, '%Y-%m-%d').date()
                        # print('forecat date', report_date, 'report date', report_date)
                        five_date = (report_date + datetime.timedelta(days=5)).strftime('%Y-%m-%d')
                        ten_date = (report_date + datetime.timedelta(days=10)).strftime('%Y-%m-%d')
                        fifty_date = (report_date + datetime.timedelta(days=15)).strftime('%Y-%m-%d')
                        therty_date = (report_date + datetime.timedelta(days=30)).strftime('%Y-%m-%d')
                        sixty_date = (report_date + datetime.timedelta(days=60)).strftime('%Y-%m-%d')
                        ninty_date = (report_date + datetime.timedelta(days=90)).strftime('%Y-%m-%d')

                        # print('code', code, report_date)
                        print(code,'获取报告日价格')
                        report_hist=ts.get_hist_data(code, row.report_date_x, row.report_date_x)
                        # print('report_hist',report_hist)
                        if( isinstance(report_hist, pd.DataFrame) and (report_hist.shape[0]>0)):
                                row['report_close']=report_hist['close'].mean()
                                # 取报告日5日收盘价平均值
                                five_df_hist=ts.get_hist_data(code, row.report_date_x, five_date)
                                if five_df_hist.shape[0]>0:
                                        row.close_5=five_df_hist['close'].mean()
                                        # print(code, '5日收盘价平均值')
                                # 取报告日5-10日收盘价平均值
                                ten_df_his=ts.get_hist_data(code, five_date, ten_date)
                                if ten_df_his.shape[0] >0 :
                                        row.close_10=ten_df_his['close'].mean()
                                # 取报告日5-10日收盘价平均值
                                fifty_df_his = ts.get_hist_data(code, ten_date, fifty_date)
                                if fifty_df_his.shape[0]>0:
                                        row.close_15=fifty_df_his['close'].mean()
                                # 取报告日5-10日收盘价平均值
                                therty_df_his = ts.get_hist_data(code, fifty_date, therty_date)
                                if therty_df_his.shape[0] >0:
                                        row.close_30=therty_df_his['close'].mean()
                                # 取报告日5-10日收盘价平均值                                # 取报告日5-10日收盘价平均值
                                sixty_df_his = ts.get_hist_data(code, therty_date, sixty_date)
                                if sixty_df_his.shape[0] >0:
                                        row.close_60=sixty_df_his['close'].mean()
                                # 取报告日5-10日收盘价平均值
                                ninty_df_his = ts.get_hist_data(code, sixty_date, ninty_date)
                                row.close_90=ninty_df_his['close'].mean()


        return  df_forecast_report




def get_forecast_and_report( year , quarter ):
        df_forecast = ts.forecast_data(year, quarter)
        df_forecast.drop_duplicates('code', keep='first')
        print('forecast', df_forecast.shape, df_forecast.columns )
        df_forecast.drop(['name'], axis=1, inplace=True)
        print( 'forecast',df_forecast.shape, df_forecast.columns)

        df_report = ts.get_report_data(year, quarter)
        df_report.drop_duplicates('code', keep='first')
        print('report', df_report.shape, df_report.columns)
        df_report['report_date']= df_report['report_date'].apply(lambda x: str(year)+'-'+x)
        print('report', df_report.shape, df_report.columns)



        df_forecast_report= pd.merge( df_report, df_forecast, on='code', how='left')
        print('forecast_report', df_forecast_report.shape, df_forecast_report.columns )

        df_forecast_report['forecast_close']=None
        df_forecast_report['report_close']=None
        df_forecast_report['close_5']=None
        df_forecast_report['close_10']=None
        df_forecast_report['close_15']=None
        df_forecast_report['close_30']=None
        df_forecast_report['close_60']=None
        df_forecast_report['close_90']=None
        print( df_forecast_report.shape)

        return  df_forecast_report


if __name__ == "__main__":
    df = get_forecast_and_report(2020, 3)
    engine = create_engine('sqlite:///foo.db')
    print(df)
    df.to_sql('report'+'_'+'2020'+'_'+'3', engine)





