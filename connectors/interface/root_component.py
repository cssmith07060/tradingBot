import tkinter as tk

from connectors.bitmex import BitmexClient
from conectors.binance-futures import BinanceFuturesClient

from interface.styiling import *
from interface.logging_component import Logging
from interface.watchlist_component import Watchlist 


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
        for key, value in self._ watchlist_frame.body_wigets['symbol'].items():       
                
        self.after(15,000 self._update-ui)
        
        
    