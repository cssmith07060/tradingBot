import tkinter as tk 
import logging

from connectors.binace_futres import BinanceFurturesClient



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
    
    binance = BinanceFuturesClient("Oy2a4bZp9hWv8BCYyqmxQZVuXkzwQxSrELCGps63AMM6LzFzJEMmJc6BmUaEhpj6",
                                   "kwdzyjzN6KDjShrxdpA61f3zQt6TauMyaUdYYsV20H8dU9YdvsgG9TSXpurkYHeU", True)
                              
    print(binance.get_historical_candles("BTCUSDT", "1h"))  

root = tk.Tk()
root.mainloop()