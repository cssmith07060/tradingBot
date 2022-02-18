class Balance:
    def __init__(self,info):
        self.inital_margin = float(info['initialMargin'])
        self.maintenance_margin = float(info['mainMargin'])
        self.margin_balance = float(info['marginBlance'])
        self.wallet_balance = float(info['walletBalance'])
        self.unrealized_pnl = float(info['unrealizedProfit'])



class Candle:
    def __init__(self, candle_info):
        self.timestamp = candle_info[0]
        self.open = float(candle_info [1])
        self.high = float(candle_info [2])
        self.low = float(candle_info [3])
        self.close = float(candle_info [4])
        self.volume = float(candle_info [5])


class Contract:
    def __init__(self, contract_info, exchange):
     if exchange == "binance":
        self.symbol = contract_info['symbol']
        self.base_asset = contract_info['baseAsset']
        self.quote_asset = contract_info['quoteAsset']
        self.price_decimals = contract_info['pricePrecison']
        self.quantity_decimals = contract_info['quantityPrecision']
     
     
     elif: exchange == "bitmex":
         self.symbol = contract_info['symbol']
        self.base_asset = contract_info['rootSymbol']
        self.quote_asset = contract_info['quoteCurrency']
        self.price_decimals = contract_info['tickSize']
        self.quantity_decimals = contract_info['lotSize']   


class OrderStatus:
    def __init__(self, order_info):
        self.order_id = info['orderId']
        self.status = order_info['status']
        self.avg_price = float(order_info['avgPrice'])




