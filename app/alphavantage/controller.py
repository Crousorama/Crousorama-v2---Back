import requests


def get_stock_from_yahoo(stock):
    r = requests.get(
        f'https://query1.finance.yahoo.com/v8/finance/chart/{stock}?region=FR&lang=fr-FR&interval=1d&range=1d&corsDomain=fr.finance.yahoo.com')
    r_json = r.json()
    return {
        "symbol": r_json['chart']['result'][0]['meta']['symbol'],
        # "open": float(r_json['Global Quote']['02. open']),
        # "high": float(r_json['Global Quote']['03. high']),
        # "low": float(r_json['Global Quote']['04. low']),
        "price": r_json['chart']['result'][0]['meta']['regularMarketPrice'],
        # "volume": int(r_json['Global Quote']['06. volume']),
        # "latest_trading_day": r_json['Global Quote']['07. latest trading day'],
        "previous_close": r_json['chart']['result'][0]['meta']['chartPreviousClose'],
        # "change": float(r_json['Global Quote']['09. change']),
        # "change_percent": r_json['Global Quote']['10. change percent'],
    }