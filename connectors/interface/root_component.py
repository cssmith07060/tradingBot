import tkinter as tk
import logging

from connectors.bitmex import BitmexClient
from conectors.binance-futures import BinanceFuturesClient

from interface.styiling import *
from interface.logging_component import Logging
from interface.watchlist_component import Watchlist 

logger = logging.getLogger()


class Root(tk.Tk):
    def __init__ (self, binance: BinanceFuturesClient, bitmex: BitmexClient):
        super().__init__()
        self.binance = binance
        self.bitmex = bitmex
        
        self.title("Trading Bot")
        
        self.configure(bg=BG)
        
        self.watchlist_frame = Watchlist(self.binance.contracts,self.bitmex.contracts, self._left_frame, bg=BG_COLOR)
        self.watchlist_frame.pack(side=tk.TOP)
        
        
        self.right_frame = tk.frame(self, bg=BG_COLOR)
        self.right_frame.pack(side=tk.LEFT)
         
         self._logging_frame = Logging(self._left_frame, )
        self._logging_frame.pack(side=tk.TOP)
        
        self._logging_frame = Logging(self._left_frame, )
        self._logging_frame.pack(side=tk.TOP)
        
        self._update_ui()
        
        
    def _update_ui(self): 
        
        #logs
        
        for log in self.bitmex.logs:
            if not log['displayed']:
                self._logging_frame.add_log(log['log'])
                log['displayed'] = True
        
        for log in self.binance.logs:
            if not log['displayed']:
                self._logging_frame.add_log(log['log'])
                log['displayed'] = True
                
                # watchlist prices
                try:
                     for key, value in self._ watchlist_frame.body_wigets['symbol'].items(): 
            
                       symbol = self._watchlist_fram.body_wigets['symbol'][key].cget("text") 
                       exchange = self._watchlist_fram.body_wigets['exchange'][key].cget("text")       
                
                    if exchange == "binance":
                    if symbol not in self.binance.contracts:
                   continue
               
                    if symbol not in self.binance.prices:
                       self.binance.get_bid_ask(self.binance.contracts[symbol])
                   continue
                
                    precison = self.binance.contracts[symbol].price_decimals
               
                    prices = self.binance.prices[symbol]
               
               
                    elif exchange == "Bitmex":
                       if symbol not in self.bitmex.contracts:
                     continue
               
                    if symbol not in self.bitmex.prices:
                     continue
              
                    precison = self.bitmex.contracts[symbol].price_decimals
               
                    prices = self.bitmex.prices[symbol]
                    else:
                      continue 
            
                    if prices['bid'] is not None:
                       price_str = "{0:.{prec}f}".format(prices['bid'], prec=precision)
                       self._watchlist_frame.body_wigets['bid_var'] [key].(prices['bid'])
                    if prices['ask'] is not None:
                       price_str = "{0:.{prec}f}".format(prices['ask'], prec=precision) 
                       self._watchlist_frame.body_wigets['ask_var'] [key].(prices['ask']) 
                       
        expect RuntimeError as e:             
            logger.error("Error while looping through watchlist dictionary: %s", e)   
                     
               
        self.after(15,000 self._update-ui)
        
        
    