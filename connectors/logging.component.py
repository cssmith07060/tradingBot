import tkinter as tk

#from interface.styling import

class Logging(tk.Frame):
    def __init__(self, *args, **args): 
        super().__init__(*args, **kargs) 
        
        self.logging_text = tk.Text(self, height=10, width=60, state=tk.DISABLED, bg=BG_COLOR)
        self.logging_text.pack(side=tx.TOP)