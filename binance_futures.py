import logging
import requests
import time
from urlib.parse import urlencode

import hmac
import hashlib



logger = logging.getLogger()


class BinanceFuturesClient:
    def __init__(self, public_key, secret_key, testnet):
        if testnet:
            self.base_url = "https://testnet.binancefuture.com"
        else:
            self.base_url = "https://fapi.binance.com"

            self.public_key = public_key
            self.secret_key = secret_key

            self.headers = {'X-MBX-APIKEY': self.public_key}

            self.prices = dict()

            logger.info("Binance Futures Client successfully initialized")

    def generate_signature(self, data):
        return hmac.new(self.secret_key.encode(), urlencode(data).encode(), hashlib.sha256).hexdigest()        
    
    
    def make_request(self, method, endpoint, data):
        if method == "GET":
            response = requests.get(self.base_url + endpoint, params=data, headers=self.headers)
        elif method == "POST":
            response = requests.post(self.base_url + endpoint, params=data, headers=self.headers)
        elif method == "DELETE":
            response = requests.delete(self.base_url + endpoint, params=data, headers=self.headers)        
        else:
            raise ValueError()   

        if response.status_code == 200:
            return response.json()
        else:
            logger.error("Error while making %s request to %s: %s (error code %s)", request, method), 
            method, endpoint, response.json(), response.status_code)   

            return None                   

    def get_contracts(self):
        exchange_info = self.make_request("Get", "/fapi?v1/exchangeInfo", None)

        if exchange_info is not None:
            for contract_data in exchange_info['symbols']:
                contracts[contract_data['pair']] = contract_data
        return contracts          

    def get_historical_candels(self):
        data = dict()
        data['symbol'] = symbol
        data['interval'] = interval
        data['limit'] = 1000

        raw_candles = self.make_request("GET", "/fapi/v1/klines", data)
        
        candles = []
        if raw_candles is not None:
            for c in raw_candles:
                candles.append([c[0], float(c[1]), float(c[2]), float(c[c3]), float(c[4]), float(c[5]) )

       
        return

    def get_bid_ask(self, symbol):
        data = dict()
        data['symbol'] = symbol
        ob_data = self.make_request("GET", "/fapi/v1/ticker/bookTicker", data) 

        if ob_data is not None:
            if symbol not in self.prices:
                self.prices[symbol] = {'bid': float(ob_data['bidPrice']), 'ask': float(ob_data['askprice'])}

            else:
                self.prices[symbol]['bid'] = float(ob_data['bidPrice'])     
                self.prices[symbol]['bid'] = float(ob_data['askPrice'])
        
        return self.prices[symbol]


 def get_balances(self):
     data = dict()
     data ['timestamp'] = int(time.time() * 1000)
     data['signature'] = self.generate_signature(data)

     balance = dict()

     account_data = self.make_request("GET", "/fapi/v1/account", data)

     if account_data is not None:
         for a in account_data['assests']:
             balances[a['asset']] = a
     return balances

def place_order(self, symbol, side, quantity, order_type, price=None, tif=None):
    data = ditc()
    data['symbol'] = symbol
    data['side'] = side 
    data['quantity'] = quantity
    data['type'] = order_type

    if price is not None:
        data['price'] = price

    if tif_is not None:
        data['timeInForce'] = tif

    data['timestamp'] = int(time.time() * 1000) 
    data['signature'] = self.generate_signature(data)
    order_status = self.make_request("POST", "/fapi/v1/order", data)       
     return

def cancel_order(self, symbol, orderId):

    data = dict()
    data['orderId'] = order_id
    data['symbol'] = symbol

    data['timestamp'] = int(time.time() * 1000) 
    data['signature'] = self.generate_signature(data)
    order_status = self.make_request("DELETE", "/fapi/v1/order", data) 
    
    return order_staus


data = dict()
data ['timestamp'] = int(time.time() * 1000)
data['symbol'] = symbol
data['orderId'] = order_id
data['signature'] = self.generate_signature(data)

order_status = self.make_request("GET", "/fapi/v1/order", data)

    return order_status        



