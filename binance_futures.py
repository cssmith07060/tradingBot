import logging
import requests
import pprint


logger = logging.getLogger()

<<<<<<< HEAD
"https://testnet.binancefuture.com"
"wss://fstream.binance.com"


def get_contracts():
    response_object = requests.get("https://fapi.binance.com/fapi/v1/exchangeInfo")
    
    
    contracts = []
    
    
    
    for contract in response_object.json()['symbols']:
        contracts.append(contract['pair'])

    return contracts    


    




print(get_contracts())
=======

def get_contracts():
    response_object = requests.get("https://fapi.binance.com")
    print(response_object.status_code, response_object.json())
    pprint.pprint(response_object.json())

    get_contracts()
>>>>>>> 67f90583513f4d25a974577a7771dded7c6454e5
