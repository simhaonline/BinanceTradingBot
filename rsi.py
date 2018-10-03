# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 20:18:05 2018

@author: jackson
"""
import kunci
from time import sleep
from binance.client import Client
client = Client(kunci.api_key,kunci.api_secret)
coin = ['BTCUSDT','IOTAUSDT','EOSBTC']
i=0

total_lose = 0
total_gain = 0
order = False


klines = client.get_historical_klines(coin[2],Client.KLINE_INTERVAL_30MINUTE, "19 August, 2018")


def search(data_open , data_close):
   
    if data_open > data_close:
       global total_lose
       loss = data_open - data_close
       total_lose += float(loss)
       return total_lose
       
    
    else:
       gain = data_close - data_open
       global total_gain
       total_gain += float(gain)
       return total_gain
   




while i < len(klines):
    open1  = float(klines[i][1])
    close1 = float(klines[i][4])
    search(open1,close1) 
    i += 1

average_rs = total_gain / total_lose
rsi = 100 - 100/(1+ average_rs)
print(rsi)




    

 