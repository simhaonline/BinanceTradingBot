# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 17:46:32 2018

@author: jackson
"""
import kunci
import datetime
from time import sleep
from binance.client import Client
client = Client(kunci.api_key, kunci.api_secret)

symbol= ['BTCUSDT','IOTAUSDT','EOSBTC']
order = False
i=0
if order != True:
    while(i < len(symbol)):
        BTC=client.get_historical_klines(symbol[i], interval='30m', start_str="1 hour ago UTC")
        print(symbol[i])
        print(BTC)
        i += 1
else:
    print("do nothing")