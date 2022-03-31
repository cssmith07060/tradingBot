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

       # t = threading.Thread(target=self._start_ws)
       # t.start()

        logger.info("Bitmex Client successfully initialized")
        
        
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

        return contrscts        

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

        raw_candles = self._make_request("GEt", "/api/v1/trade/bucketed", data)

        candles = []

        if raw_candles is not None:
            for c in raw_candles:
                candles.append(Candle(c, "bitmex"))