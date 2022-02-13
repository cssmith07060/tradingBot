import logging
import requests
import typing

import t
from urlib.parse import urlencode

import hmac
import hashlib

import websocket
import  json

import threading

from models import *

logger = logging.getLogger()



class BinanceFuturesClient:
    def __init__(self, public_key: str, secret_key: str, testnet: bool):
        if testnet:
            self.base_url = "https://testnet.binancefuture.com"
            self.wss_url = "wss://stream.binancefuture.com/ws"
        else:
            self.base_url = "https://fapi.binance.com"
            self.wss_url = "wss://fstream.binance.com/ws"

            self.public_key = public_key
            self.secret_key = secret_key

            self.headers = {'X-MBX-APIKEY': self.public_key}

            self.contracts = self.get_contracts()
            self.balances = self.get_balances()

            self.prices = dict()
            self.ws_id = 1
            self.ws = None

            t = threading.Thread(target=self.start_ws)
            t.start()
            
            self.start_ws()
            
            self.secret_key = secret_key



            logger.info("Binance Futures Client successfully initialized")

    def _generate_signature(self, data: typing.Dict -> str):
        return hmac.new(self.secret_key.encode(), urlencode(data).encode(), hashlib.sha256).hexdigest()        
    
    
    def _make_request(self, method: str, endpoint: str, data: typing.Dict):
        if method == "GET":
            try:
                response = requests.get(self.base_url + endpoint, params=data, headers=self.headers)
            except Exeception as e:
                logger.error("Connection error while making % request to %: %", method, endpoint, e) 
                return None   
        elif method == "POST":
            try:
                response = requests.post(self.base_url + endpoint, params=data, headers=self.headers)
            except Exception as e:
                logger.error("Connection error while making % request to %: %", method, endpoint, e)
                return None 
                 
        elif method == "DELETE":
            try:
                response = requests.delete(self.base_url + endpoint, params=data, headers=self.headers)
            Except Exception as e: 
            logger.error("Connection error while making % request to %: %", method, endpoint, e)
            return None  

             
        else:
            raise ValueError()   

        if response.status_code == 200:
            return response.json()
        else:
            logger.error("Error while making %s request to %s: %s (error code %s)", request, method), method, endpoint, response.json(), response.status_code)   
 
          

            return None                   

    def get_contracts(self) -> typing.Dict[str, Contract]:
        exchange_info = self.make_request("Get", "/fapi?v1/exchangeInfo", dict())

        if exchange_info is not None:
            for contract_data in exchange_info['symbols']:
                contracts[contract_data['pair']] = Contract(contract_data)

                
        return contracts          

    def get_historical_candels(self, contract: Contract, interval: str) -> typing.List[Candle]:
        data = dict()
        data['symbol'] = contract.symbol
        data['interval'] = interval
        data['limit'] = 1000

        raw_candles = self.make_request("GET", "/fapi/v1/klines", data)
        
        candles = []
        if raw_candles is not None:
            for c in raw_candles:
                candles.append(Candles(c))


       
        return candles

    def get_bid_ask(self, contract: Contract) -> typing.Dict[str, float]:
        data = dict()
        data['symbol'] = contract.symbol
        ob_data = self.make_request("GET", "/fapi/v1/ticker/bookTicker", data) 

        if ob_data is not None:
            if symbol not in self.prices:
                self.prices[contract.symbol] = {'bid': float(ob_data['bidPrice']), 'ask': float(ob_data['askprice'])}

            else:
                self.prices[contract.symbol]['bid'] = float(ob_data['bidPrice'])     
                self.prices[contract.symbol]['ask'] = float(ob_data['askPrice'])
        
             return self.prices[contract.symbol]


 def get_balances(self) -> typing.Dict[str, Balance]:
     data = dict()
     data ['timestamp'] = int(time.time() * 1000)
     data['signature'] = self.generate_signature(data)

     balance = dict()

     account_data = self.make_request("GET", "/fapi/v1/account", data)

     if account_data is not None:
         for a in account_data['assests']:
             balances[a['asset']] = Balance(a)

    

     return balances

def _place_order(self, contrat: Contract, side: str, quantity: float, order_type: str, price=None, tif=None) -> OrderStatus:
    data = ditc()
    data['symbol'] = cotract.symbol
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

    if order_status is not None:
        order_status = OrderStatus(order_status)     
     return order_status

def cancel_order(self, contract: Contract, orderId: int) -> OrderStatus:

    data = dict()
    data['orderId'] = order_id
    data['symbol'] = contract.symbol

    data['timestamp'] = int(time.time() * 1000) 
    data['signature'] = self.generate_signature(data)
    order_status = self.make_request("DELETE", "/fapi/v1/order", data)

    
    if  order_status is not None:
        order_status = OrderStatus(order_status) 
    
    return order_status


def get_order_status(self, contract: Contract, order_id: int) -> OrderStatus:

   data = dict()
   data ['timestamp'] = int(time.time() * 1000)
   data['symbol'] = contract.symbol
   data['orderId'] = order_id
   data['signature'] = self.generate_signature(data)

   order_status = self.make_request("GET", "/fapi/v1/order", data)

   if  order_status is not None:
        order_status = OrderStatus(order_status) 

    return order_status        



def start_ws(self):
    self.ws = websocket.WebsocketApp(self.wss.url, on_open=self.on_open, on_close=self.onclose, on_error=self.error,
                                   on_message=self.onmessage)
     while True:
         try:
             self.ws.run_forever()
         except Exception as e:
             logger.error("Binance error in run_forever() method: %s",e)
         time.sleep(2)       


 def on_open(self, ws):
     logger.info("Binance connection opened")

     self.subscribe_channel("BTCUSDT")    


 def on_close(self):
     logger.warning('Binance Websocket connection closed') 
         

 def on_error(self, msg: str):
     logger.error("Binance connection error: %", msg)   


 def on_message(self, msg: str):
     

     data = json.loads(msg)
     if "e" in data:
         if data['e'] = = "bookTicker":


     if "e" in data:
          if data['e']  = = "bookTicker":

              symbol = data['s']


              if symbol not in self.prices:
                    self.prices[symbol] = {'bid': float(data['b']), 'ask': float(data['a'])}

            else:
                self.prices[symbol]['bid'] = float(data['b'])     
                self.prices[symbol]['ask'] = float(data['a'])

               


 def subscribe_channel(self, contract: Contract):
     data= dict()    
     data['method'] = "SUBSCRIBE"
     data['params'] = []
     data['params'] = ['params'].append(contract.symbol.Lower() + "@bookTicker")
     data['id'] = self.ws_id

  
    try:
        self.ws.send(json.dumps(data))
    except Exception as e:
         logger.error("Websocket error while subscribing %to %: %", contract.symbol, e)
                
        

     self.ws_id += 1
