import requests
from mail_notify import *


class Stock:

    def __init__(self, ticker, desired):
        self.ticker = ticker
        self.cur = 0.0
        self.max = 0.0
        self.min = 0.0
        self.desired = desired

    @staticmethod
    def import_stocks():
        response_json = requests.get("https://brapi.dev/api/quote/list")
        stock_list = response_json.json()
        stock_tickers = []
        for item in stock_list['stocks']:
            stock_tickers.append(item.get('stock'))
        return stock_tickers

    def monitor(self, msg_to):
        response_json = requests.get("https://brapi.dev/api/quote/{}".format(self.ticker))
        stock_ticker = response_json.json()
        self.cur = stock_ticker['results'][0].get('regularMarketPrice')
        self.max = stock_ticker['results'][0].get('regularMarketDayHigh')
        self.min = stock_ticker['results'][0].get('regularMarketDayLow')

        if float(self.desired) >= float(self.cur):
            send_mail("{} alcançou o valor desejado. Valor atual R${}".format(self.ticker, self.cur), self.ticker, msg_to)
            return True

        return False
