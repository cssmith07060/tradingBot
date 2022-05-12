import tkinter as tk

#from interface.styling import

class Logging(tk.Frame):
    def __init__(self, *args, **args): 
        super().__init__(*args, **kargs) 
        
        self.logging_text = tk.Text(self, height=10, width=60, state=tk.DISABLED, bg=BG_COLOR, fg FG_COLOR_2, 
                                    font= GLOBAL_FONT)
        self.logging_text.pack(side=tx.TOP)
        
        
        def add_log(self, message: str):
            self.logging_text.configure(state=tk.NORMAL)
            
            
            
            self.logging_text.configure(state=tk.DISABLED)