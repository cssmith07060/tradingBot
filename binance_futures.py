import logging
import requests



logger = logging.getLogger()


class BinanceFuturesClient:
    def __init__(self, testnet):
        if testnet:
            self.base_url = "https://testnet.binancefuture.com"
        else:
            self.base_url = "https://fapi.binance.com"

            self.prices = dict()

                logger.info("Binance Futures Client successfully initialized")
    def make_request(self, method, endpoint, data):
        if method == "GET":
            response = requests.get(self.base_url + endpoint, params=data)
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

        raw_candles = self.make_request("GET", "fapi/v1/klines", data)
        
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

