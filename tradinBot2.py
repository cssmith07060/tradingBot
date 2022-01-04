import tkinter as tk 
import logging



logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)


logger.addHandler(stream_handler)
logger.addHandler(file_handler)

<<<<<<< HEAD
=======

>>>>>>> 67f90583513f4d25a974577a7771dded7c6454e5





if _ _name_ _ == '_ _main_ _':
      
      bitmex_contracts = get_contracts()
      

  root = tk.Tk()

   i = 0 
   j = 0

  for contract in bitmex_contracts:
        label_widget = tk.Label(root, text=contract, borderwidth=1, relief=tk.SOLID)
        label_widget.grid(row=i, column=j)

        if i == 4:
              j += 1
              i = 0

        else:
            i += 1 
  root.mainloop()