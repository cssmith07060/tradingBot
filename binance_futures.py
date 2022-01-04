import logging
import requests
import pprint


logger = logging.getLogger()

"https://testnet.binancefuture.com"
"wss://fstream.binance.com"


def get_contracts():
    response_object = requests.get("https://fapi.binance.com/fapi/v1/exchangeInfo")
    
    
    contracts = []
    
    
    
    for contract in response_object.json()['symbols']:
        contracts.append(contract['pair'])

    return contracts    


    




print(get_contracts())