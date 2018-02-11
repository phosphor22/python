from binance.client import Client

#2018/1/9 修正
api_key = "***"
api_secret = "***"

client = Client(api_key, api_secret)



# 全銘柄取得
ticker = client.get_ticker(symbol="XRPBTC")

ask = ticker['askPrice']
bid = ticker['bidPrice']
        
print("■binance：" + "XRPBTC")
print('bid:'+ str(bid))
print('ask:'+ str(ask))
