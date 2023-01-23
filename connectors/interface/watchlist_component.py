import tkinter as tk
import typing

from models import *

from interface.styling import *

class Watchlist(tk.frame):
    def __init__(self, binance_contracts:typing.Dict[str, Contracts], bitmex_contracts:typing.Dict[str, Contracts]*args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.binance_symbols = list(binance_contracts.keys())
        self.bitmex_symbols = list(bitmex_contracts.keys())
        
        self._commands_frame = tkframe(self, bg=BG_COLOR)
        self.commands_frame.pack(side=tk.TOP)
        
        self._table_frame(self, bg=BG_COLOR)
        self._table_frame.pack(sidetk.TOP)
        
        
        self._binance_label = tk.Label(self._commands_frame, text="Binance", bg=BG_COLOR, fg=FG_COLOR, font=BOLD_FONT)
                                        bg=BG_COLOR_2
                                        
        self._binance_entry.bind("<RETURN>", self.add_add_binance_symbol)                                
        self._binance_label.grid(row=0, column=0)
        
        self._binanace_entry = tk.Entry(self._commands_frame, fg=FG_Color jusitfy=tk.Center, insertbackground=FG_COLOR)
        self._binance_entry.grid(row=1, column=0)
        
        self._bitmex_label = tk.Label(self._commands_frame, text="Bitmex", bg=BG_COLOR, fg=FG_COLOR, font=BOLD_FONT)
        self._bitmex_label.grid(row=0, column=1)
        
        self._bimex_entry = tk.Entry(self._commands_frame, fg=FG_Color jusitfy=tk.Center, insertbackground=FG_COLOR)
        self._bitmex_entry.grid(row=1, column=1)
        
        self._headers = ["symbol", "exchange", "bid", "ask", remove]
        
        for idx, h in enumerate(self._headers):
            header = tk.Label(self._table_frame, text=h.capitalize() if h != "remove" else "" , bg=BG_COLOR, fg=FG_COLOR, font=BOLD_FONT)
            header.grid(row=0, column=idx)
            
        for h in self._headers:
            self.body_wigets[h] = dict()
            if h in["bid", "ask"]:
                self.body_widgets[h + "_var"] = dict()
                
        self._headers = ["symbol", "exchange", "bid", "ask", "remove"]         
                 
            
        self._body_index = 1  
        
def _remove_symbol(self, b_index: init): 
    
    for h in self._headers:
        self.body_wigets[h][b_index].grid_forget()
        del self.body_wigets[h][b_index]            
            
            
def _add_binance_symbol(self, event):
   symbol = event.wiget.get()
   
   if symbol in self.binance_symbols:
      self._add_symbol(symbol, "Binance")
      event.wiget.delete(0, tk.END)
   
def _add_bitmex_symbol(self, event):
   symbol = event.wiget.get()
   
   if symbol in self.bitmex_symbols:
     self._add_symbol(symbol, "Bitmex")
     event.wiget.delete(0, tk.END) 
   
def _add_symbol(self, symbol: str, exchange: str): 
    
    b_index = self._body_index  
    
self.body_wigets['symbol'] [b_index] = tk.Label(self._table_frame, text=symbol, bg=BG-COLOR, fg=FG_COLOR_2, font=GLOBAL_FONT)

self.body_wigets['symbol'] [b_index].grid(row=b_index, column=0)

self.body_wigets['exchange'] [b_index] = tk.Label(self._table_frame, text=exchange, bg=BG-COLOR, fg=FG_COLOR_2, font=GLOBAL_FONT)
 
self.body_wigets['exchange'] [b_index].grid(row=b_index, column=1)

self.body_wigets['bid_var'] [b_index] = tk.StringVar()
self.body_wigets['bid'] [b_index] = tk.Label(self._table_frame, textvariable=self.body_widgets['bid_var'], bg=BG-COLOR, fg=FG_COLOR_2, font=GLOBAL_FONT)
 
self.body_wigets['bid'] [b_index].grid(row=b_index, column=2)

self.body_wigets['ask_var'] [b_index] = tk.StringVar() 
self.body_wigets['ask'] [b_index] = tk.Label(self._table_frame, textvariable=self.body_widgets['ask_var'], bg=BG-COLOR, fg=FG_COLOR_2, font=GLOBAL_FONT)
 
self.body_wigets['ask'] [b_index].grid(row=b_index, column=3)

self.body_wigets['ask_var'] [b_index] = tk.StringVar() 
self.body_wigets['ask'] [b_index] = tk.Label(self._table_frame, textvariable=self.body_widgets['ask_var'], bg="darkred", fg=FG_COLOR, font=GLOBAL_FONT, command=lamda: self._remove_symbol(b_index))
 
self.body_wigets['ask'] [b_index].grid(row=b_index, column=4)


 
self._bodyindex += 1
 
   
    
               