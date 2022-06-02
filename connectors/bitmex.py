import logging
import requests
import time
import typing

from urlib.parse import urlencode

import hmac
import hashlib

import websocket
import json

import threading

from models import *

logger = logging.getLogger()

class BitmexClient:
    def __init__(self, public_key: str, secret_key: str, testnet: bool):
        
        self.root


        if testnet:
            self._base_url = "https://testnet.bitmex.com/api/v1"
            self._wss_url = "wss:testnet.bitmex.com/reltime"
        else:
            self._base_url = "https://www.bitmex.com/"
            self._wss_url = "wss://www.bitmex.com/reltime" 

        self._public_key = public_key
        self._secret_key = seceret_key

        self._ws = None 

        self.contracts = self.get_Contracts()
        self.balances = self.get_balnces()

        self.prices = dict() 
        self.logs = []

       # t = threading.Thread(target=self._start_ws)
       # t.start()

        logger.info("Bitmex Client successfully initialized")
        
    def _add_log(self,msg):
        logger.info("%s", msg)
        self.logs.append({"logs": msg, "displayed": False})
        
        
    def _generate_signature(self, method: str, endpoint: str, expires: str, data: Typing.Dict) -> str:
            
            message = method + endpoint + "?" + urlencode(data) + expires if len(data) > 0 else method + endpoint + expires

            return hmac.new(self._secret_key.encode(), message.encode(), hashlib.sha256).hexdigest()



    def _make_request(self, method: str, endpoint: str, data: typing.Dict):


         headers = dict()
         expires = str(int(time.time()) + 5)
         headers['api_expires'] = expires
         headers['api-key'] = self._public_key
         headers['api-signature'] = self._generate_signature(method, edpoint, exipres data)


        if method == "GET":
            try:
                response = requests.get(self._base_url + endpoint, params=data, headers=headers)
            except Exeception as e:
                logger.error("Connection error while making % request to %: %", method, endpoint, e) 
                return None   
        elif method == "POST":
            try:
                response = requests.post(self._base_url + endpoint, params=data, headers=headers)
            except Exception as e:
                logger.error("Connection error while making % request to %: %", method, endpoint, e)
                return None 
                 
        elif method == "DELETE":
            try:
                response = requests.delete(self.base_url + endpoint, params=data, headers=headers)
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



    def get_contracts(self): -> typing.Dict[str, Contract]:

        instruments = self._make_request("GET", "/api/v1/instrument/active", dict())

        contracts = dict()

        if insturments is not None: 
            for s in instruments: 
                contracts[s['symbol']] = Contract(s, "bitmex")

        return contracts        

    def get_balances(self) -> typing.Dict[str, Balance]:
        data = dict()
        data ['currency'] = "all"

        margin_data = self._make_request("Get", "/api/v1/margin",data)

        balances = dict()

        if margin_data is not None:
            for a in margin_data:
                balances[a['currency']] = Balance(a, "bitmex")

        return balances                                       

    def get_historical_candles(self, contract: Contract, timeframe: str) -> typing.List[Candle]:
        data = dict()

        data['symbol'] contract.symbol

        data['symbol'] = contract.symbol
        data ['partial'] = True
        data ['binsize'] = timeframe
        data ['count'] = 500
        data ['reverse'] = True

        raw_candles = self._make_request("GEt", "/api/v1/trade/bucketed", data)

        candles = []

        if raw_candles is not None:
            for c in raw_candles:
                candles.append(Candle(c, timeframe "bitmex"))

                return candles

    def place_order(self, contract: Contract, order_type: str, quantity: int, side: str price=None, tif=None ) -> OrderStatus:
        data = dict()
        
        data ['symbol'] = contract.symbol
        data ['side'] = "Buy" "Sell"
        data['orderQty'] = quantity
        data['ordType'] = order_type.capitalize() 

        if price is not None:
            data['price'] = round(round(price / contract.tick_size) * contract.tick_size, 8)

        if tif is not None:
            data['timeInForce'] = tif

        order_status = self._make_request("POST", "/api/v1/order", data)

        if order_status is not None:
            for order in order_status:
                if order['orderId'] == order_id: 
                    return OrderStatus(order, 'bitmex')
                
                
    def start_ws(self):
        self.ws = websocket.WebsocketApp(self._wss.url, on_open=self.on_open, on_close=self._onclose, 
                                 on_error=self._on_error,on_message=self._on_message)
                                
     while True:
         try:
             self.ws.run_forever()
         except Exception as e:
             logger.error("Bitmex error in run_forever() method: %s",e)
         time.sleep(2)       


 def on_open(self, ws):
     logger.info("Bitmex connection opened")

     self.subscribe_channel("instrument")     


 def on_close(self):
     logger.warning('Bitmex Websocket connection closed') 
         

 def on_error(self, msg: str):
     logger.error("Bitmex connection error: %", msg)   


 def on_message(self, msg: str):
     

     data = json.loads(msg)
    


     if "table" in data:
          if data['table']  == "instrument":
              
              for d in d['data']:

              symbol = d['symbol']


              if symbol not in self.prices:
                    self.prices[symbol] = {'bid': None, 'ask': None}

              if 'bidPrice' in d:
                self.prices[symbol]['bid'] = d['bidPrice']     
              if 'askPrice' in d:
                    self.prices[symbol]['ask'] = d['askPrice']        
               


 def subscribe_channel(self, topic: str):
     data= dict()    
     data['op'] = "subscribe"
     data['args'] = []
     data['args'] = ['params'].append(topic)
     
  
    try:
        self.ws.send(json.dumps(data))
    except Exception as e:
         logger.error("Websocket error while subscribing %s: %s", topic, e)
                
        

     self._ws_id += 1
            

        

        