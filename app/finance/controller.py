import requests
from bs4 import BeautifulSoup

INTERVAL_MAPPING = {
    "1d": "2m", # 2m
    "5d": "15m",
    "1mo": "30m",
    "6mo": "1d",
    "ytd": "1h",
    "1y": "1d",
    "5y": "1wk",
    "max": "1mo",
}


def get_stock_from_yahoo(stock, date_range):
    print(f'https://query1.finance.yahoo.com/v8/finance/chart/{stock}?region=FR&interval={INTERVAL_MAPPING[date_range]}&lang=fr-FR&range={date_range}&corsDomain=fr.finance.yahoo.com')
    r = requests.get(
        f'https://query1.finance.yahoo.com/v8/finance/chart/{stock}?region=FR&interval={INTERVAL_MAPPING[date_range]}&lang=fr-FR&range={date_range}&corsDomain=fr.finance.yahoo.com')
    r_json = r.json()
    symbol_data = requests.get(f'http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={stock}&region=1&lang=en')
    symbol_data = symbol_data.json()
    try:
        return {
            "symbol": r_json['chart']['result'][0]['meta']['symbol'],
            "full_name": symbol_data['ResultSet']['Result'][0]['name'] if len(symbol_data['ResultSet']['Result']) > 0 else "",
            "price": r_json['chart']['result'][0]['meta']['regularMarketPrice'],
            "currency": r_json['chart']['result'][0]['meta']['currency'],
            "previous_close": r_json['chart']['result'][0]['meta']['chartPreviousClose'],
            "validRanges": r_json['chart']['result'][0]['meta']['validRanges'],
            "timestamps": r_json['chart']['result'][0]['timestamp'] if 'timestamp' in r_json['chart']['result'][0] else [],
            "prices": r_json['chart']['result'][0]['indicators']['quote'][0],
        }
    except IndexError as e:
        print("symbol_data")
        print("symbol_data")
        print("symbol_data")
        print(symbol_data)
        print("r_json")
        print("r_json")
        print("r_json")
        print(r_json)
        raise e


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

                        cell_link_soup = BeautifulSoup(str(cell), features="html.parser")
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