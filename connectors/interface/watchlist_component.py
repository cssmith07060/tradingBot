import tkinter as tk

from interface.styling import *

class Watchlist(tk.frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self._commands_frame = tkframe(self, bg=BG_COLOR)
        self.commands_frame.pack(side=tk.TOP)
        
        self._table_frame(self, bg=BG_COLOR)
        self._table_frame.pack(sidetk.TOP)
        
        
        self._binance_label = tk.Label(self._commands_frame, text="Binance", bg=BG_COLOR, fg=FG_COLOR, font=BOLD_FONT)
        self._binance_label.grid(row=0, column=0)
        
        self._binanace_entry = tk.Entry(self._commands_frame, fg=FG_Color jusitfy=tk.Center, insertbackground=FG_COLOR)
        self._binance_entry.grid(row=1, column=0)
        
        self._bitmex_label = tk.Label(self._commands_frame, text="Bitmex", bg=BG_COLOR, fg=FG_COLOR)
        self._bitmex_label.grid(row=0, column=1)
        
        self._bimex_entry = tk.Entry(self._commands_frame, fg=FG_Color jusitfy=tk.Center, insertbackground=FG_COLOR)
        self._bitmex_entry.grid(row=1, column=1)