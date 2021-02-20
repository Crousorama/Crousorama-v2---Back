import requests
from bs4 import BeautifulSoup


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


def search_stocks(search):
    r = requests.get(f"https://query1.finance.yahoo.com/v1/finance/search?q={search}&quotesCount=5")
    r_json = r.json()
    return r_json['quotes']


def get_palmares():
    req = requests.get('https://m.investir.lesechos.fr/marches/palmares/palmares.php')
    html = req.text
    soup = BeautifulSoup(html, features="html.parser")
    blocs = soup.findAll('div', {'class': ['row', 'indice']})
    rows = []
    for b in blocs:
        row_soup = BeautifulSoup(str(b))
        tmp = {
            'indice': row_soup.find('div', {'class': 'nom-indice'}).text,
            'meta': row_soup.find('span', {'class': 'place-heure'}).text,
            'value': row_soup.find('span', {'class': 'val-indice'}).text,
            'variation': row_soup.find('span', {'class': 'var-indice'}).text,
        }
        if not palmares_already_pushed(tmp['indice'], rows):
            rows.append(tmp)
    return rows


def palmares_already_pushed(quote, array):
    matches = [x for x in array if x['indice'] == quote]
    return len(matches) > 0


def get_palmares_dividend():
    dividends = []
    for page in [1, 2, 3]:
        req = requests.get('https://www.boursorama.com/bourse/actions/palmares/dividendes/page-{}'
                           .format(page if page is not None else '1'))
        html = req.text
        soup = BeautifulSoup(html, features="html.parser")
        rows = soup.findAll('tr', {'class': 'c-table__row'})
        headers = []
        for idx, row in enumerate(rows):
            tmp = {}
            for idx_cell, cell in enumerate(row.contents):
                if idx == 0:
                    headers.append(cell.text)
                else:
                    try:
                        tmp[headers[idx_cell]] = parse_spaces(cell.text)

                        cell_link_soup = BeautifulSoup(str(cell))
                        link = cell_link_soup.find('a')
                        if link:
                            splitted = link.attrs.get('href').split('/')
                            tmp['symbol'] = splitted[len(splitted) - 2].replace('1rP', '')
                    except AttributeError as e:
                        continue
            if tmp != {}:
                dividends.append(tmp)
    return dividends


def parse_spaces(string):
    return remove_jumps(string).replace(' ', '') if '\n' in string else string


def remove_jumps(string):
    return string.replace('\n', '')