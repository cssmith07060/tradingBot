import logging
import requests
import pprint


logger = logging.getLogger()


def get_contracts():
    response_object = requests.get("https://fapi.binance.com")
    print(response_object.status_code, response_object.json())
    pprint.pprint(response_object.json())

    get_contracts()