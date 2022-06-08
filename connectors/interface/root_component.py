import tkinter as tk

from connectors.bitmex import BitmexClient
from conectors.binance-futures import BinanceFuturesClient

from interface.styiling import *


class Root(tk.Tk):
    def __init__ (self, binance: BinanceFuturesClient, bitmex: BitmexClient):
        super().__init__()
        self.title("Trading Bot")
        
        self.configure(bg=BG)
        
        self.left_frame = tk.frame(self, bg=BG_COLOR)
        self.left_frame.pack(side=tk.LEFT)
        
        
        self.right_frame = tk.frame(self, bg=BG_COLOR)
        self.right_frame.pack(side=tk.LEFT)
        
        self._logging_frame = Logging(self._left_frame, )
        self._logging_frame.pack(side=tk.TOP)
        
    def _update_ui(self):
        
        for log in self.bitmex.logs    
        
        
        
        
    