import requests
import datetime
import argparse
import sys


urls = {
    'dzisiaj': 'http://api.nbp.pl/api/cenyzlota/today',
    'data': 'http://api.nbp.pl/api/cenyzlota/{date}'
}


def get_price_today():
    
    price = requests.get(urls['dzisiaj'])
    if price.status_code == 200:
        return price.json()[0]['cena']
    else:
        price.raise_for_status()


def get_price_date(data):
    
    try:
        temp = datetime.date.fromisoformat(data)
    except ValueError:
        raise ValueError('Niepoprawny format parametru daty, proszę podać datę w formacie: RRRR-MM-DD')
    
    price = requests.get(urls['data'].format(date=temp))
    if price.status_code == 200:
        return price.json()[0]['cena']
    else:
        price.raise_for_status()


def main(arguments):
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--d', help='Data w formacie RRRR-MM-DD', metavar='Data')
    args = parser.parse_args(arguments[1:])

    if args.d:
        temp = get_price_date(args.d)
        print(f'Cena złota w dniu {args.d} wynosiła {temp}.')
    else:
        print(f'Cena złota wynosi dzisiaj {get_price_today()}.')


if __name__ == "__main__":
    main(sys.argv)
