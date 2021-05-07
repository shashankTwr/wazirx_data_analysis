import requests
import json
import pandas as pd
from datetime import datetime

## loading the ticker price 
response = requests.get("https://api.wazirx.com/api/v2/tickers")
ticker_data = response.json()
print(type(ticker_data))

## loading the dictionary into a list of dictionary object to convert it into a dataframe
price_list = []
for key,value in ticker_data.items():
    price_list.append(value)
print(price_list)

df = pd.DataFrame(price_list)
df['at']= pd.to_datetime(df['at'],unit = 's')
df['dates'] = pd.to_datetime(df['at']).dt.date
df['time'] = pd.to_datetime(df['at']).dt.time


df_inr = df[df['quote_unit'] == 'inr']
df_usdt = df[df['quote_unit'] == 'usdt']
df_btc = df[df['quote_unit'] == 'btc']
df_wrx = df[df['quote_unit'] == 'wrx']

time_curr = datetime.now().strftime("%Y%m%d-%H%M%S")
print(time_curr+"-inr")

df_inr.to_csv("./data/inr/"+time_curr+"-inr.csv",index=False)
df_usdt.to_csv("./data/usdt/"+time_curr+"-usdt.csv",index=False)
df_btc.to_csv("./data/btc/"+time_curr+"-btc.csv",index=False)
df_wrx.to_csv("./data/wrx/"+time_curr+"-wrx.csv",index=False)