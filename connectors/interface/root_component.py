import tkinter as tk

from interface.styiling import *


class Root:
    def __init__ (self):
        super().__init__()
        self.title("Trading Bot")
        
        self.configure(bg=BG)
        
        self.left_frame = tk.frame(self, bg=BG_COLOR)
        self.left_frame.pack()
        
        
    