import os
#This example uses Python 2.7 and the python-request library.

from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
my_secret = os.environ['COINMARKET_API_KEY']
parameters = {'start': '1', 'limit': '50', 'convert': 'USD'}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': my_secret,
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  print(data)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)
