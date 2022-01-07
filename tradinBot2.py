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






if __name__ == '__main__':
      
      bitmex_contracts = get_contracts()
      

  root = tk.Tk()
  root.configure(bg="gray12")

   i = 0 
   j = 0

   calbri_font = ("calibri", 11, "normal")

  for contract in bitmex_contracts:
        label_widget = tk.Label(root, text=contract, borderwidth=1, relief=tk.SOLID, width=13, font= calibri_font)
        label_widget.grid(row=i, column=j, sticky=)

        if i == 4:
              j += 1
              i = 0

        else:
            i += 1 
  root.mainloop()