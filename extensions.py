import requests
import json
from config import keys


class APIException(Exception):
    pass


class get_price:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты: {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту: {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту: {base}')

        try:
            amount = int(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать кол-во: {amount}')

        if amount > 0:
            pass
        else:
            raise APIException(f'Некорректное кол-во: {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = round(json.loads(r.content)[keys[base]] * amount, 2)

        return total_base