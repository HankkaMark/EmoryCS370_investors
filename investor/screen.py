#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Noc  8 10:23:53 2021

@author: tracy
"""


import pandas_datareader as pdr
from yahoo_fin import stock_info as si
import yfinance as yf
import pandas as pd
import datetime
import time
import ssl
 
ssl._create_default_https_context = ssl._create_unverified_context

def job():
    print("-----------------开始运行----------------")

# 
    tickers = si.tickers_sp500()


    start = datetime.datetime.now() - datetime.timedelta(days=365)
    end = datetime.datetime.now()

    sp500=pdr.DataReader('^GSPC', 'yahoo', start, end)
    sp500['Percent Change'] = sp500['Adj Close'].pct_change()
    sp500_return=(sp500['Percent Change'] + 1).cumprod()[-1]

    return_list=[]

    return_df=pd.DataFrame(columns=["Stock", "Price", "Score", "PE_Ratio", "SMA_150","SMA_200", "52 Week Low", "52 Week High"])
    count=0



    # Dividing the cumulative return of each stock over the cumulative return of the index 
    for t in tickers:
        data = pdr.DataReader(t, 'yahoo', start, end)
        data.to_csv(f'{t}.csv')

        data['Percent Change'] = data['Adj Close'].pct_change()
        # print(data['Adj Close'])
        pc=(data['Percent Change'] + 1).cumprod()
        # print(pc[-1])
        st_return = pc[-1]
        
        rs=st_return / sp500_return
        # print(rs)
        returns_compared = round(rs, 3)
        return_list.append(returns_compared)
        

        # count+=1

        # if count==20:
        #     break
    #
            
    top_df = pd.DataFrame(list(zip(tickers, return_list)), columns=['Ticker', 'Returns Compared'])
    top_df["Score"] = top_df["Returns Compared"].rank(pct=True) * 100



    top_df = top_df[top_df["Score"]>= top_df["Score"].quantile(.90)]




    for stock in top_df['Ticker']:    
        try:
            df = pd.read_csv(f'{stock}.csv', index_col=0)
            ma = [50, 150, 200]
            
            for m in ma:
                name="SMA_"+f'{m}'
                df[name] = df['Adj Close'].rolling(window=m).mean()
            
            
            current_price = df["Adj Close"][-1]
            pe_ratio=si.get_quote_table(stock)['PE Ratio (TTM)']
            
            # print(pe_ratio)
            
            # print(df["SMA_50"])
            ma_50 = df["SMA_50"][-1]
            ma_150 = df["SMA_150"][-1]
            ma_200 = df["SMA_200"][-1]
            
            # print(df["Low"])
            # print(df["Low"][-365:])
            # print(df["Low"][-260:])
            low_52_week = min(df["Low"][-260:])
            high_52_week = max(df["High"][-260:])
            
            # print(top_df['Ticker']==stock]["Score"])
            score=top_df[top_df['Ticker']==stock]["Score"].tolist()[0]
            score = round(score)
            
            
            
            
            # The current stock price is above both the 150-day (30-week) and the 200-day (40-week) moving average price lines.
            
            c1 = current_price > ma_150 > ma_200
            
            
            #The 150-day moving average is above the 200-day moving average.
            c2 = ma_150 > ma_200
            
            # The 50-day (10-week) moving average is above both the 150-day and 200-day moving averages.

            c3 = ma_50 > ma_150 > ma_200
            
            # The current stock price is trading above the 50-day moving average.
            c4 = current_price > ma_50
            
            #The current stock price is at least 30 percent above its 52-week low.
            c5 = current_price >= (1.3*low_52_week)
            
            #The current stock price is within at least 25 percent of its 52-week high (the closer to a new high the better).
            c6 = current_price >= (.75*high_52_week)
            
        
            if(c1 and c2 and c3 and c4 and c5 and c6):
                return_df = return_df.append({"Stock": stock, "Price": current_price, "Score": score ,"PE_Ratio": pe_ratio, "SMA_150": ma_150, "SMA_200": ma_200, "52 Week Low": low_52_week, "52 Week High": high_52_week}, ignore_index=True)
                
                # print (stock)
                

        except Exception as e:
            print(f'{e} for {stock}')

            
            

    return_df = return_df.sort_values(by="Score", ascending=False)


    pd.set_option('display.max_columns', 10)

    print(return_df)



    return_df.to_csv("stock.csv")
    print("-----------------运行结束----------------")


import schedule
import time


#schedule.every(10).seconds.do(job)
schedule.every(2).hours.do(job)


while True:
    schedule.run_pending()
    time.sleep(1)


