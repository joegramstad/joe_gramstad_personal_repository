from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import csv

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/info'
parameters = {
    'aux': 'id,name,symbol,tags,platform,category,date_launched',
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': 'cb5d457e-751b-4f0d-9f5e-de50cb591066',
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
# data = json.loads(response.text)
# data = data['data']


with open('response.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'name', 'symbol', 'tags', 'platform', 'category', 'date_launched']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in response.json():
        writer.writerow(row)

# def get_json_response(url):
#     response = requests.get(url)
#     data = response.text
#     json_data = json.loads(data)
#     return json_data


# def main():
#     json_response = get_json_response('https://pro-api.coinmarketcap.com/v1/cryptocurrency/map')
#     print(json_response)
#
#
# main()
