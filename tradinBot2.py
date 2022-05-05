import tkinter as tk 
import logging

from connectors.binace_futres import BinanceFurturesClient
from connectors.bitmex import BitmexClient

from interface.root_component import Root



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

    bitmex = BitmexClient("uXr1711wD-3pvEpXjlkNFx", "GEIkARqi2QZh7OV77T28M2Y0zxSBh_rNGhRJIbwZAIqYCkYu", True)


root = Root()
root.mainloop()