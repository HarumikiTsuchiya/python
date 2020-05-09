import requests

url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
payload = {'city':'230010'}
tenki_data = requests.get(url, params=payload).json()
#print(tenki_data)
print(tenki_data['title'])
print(tenki_data['forecasts'][1]['date'])
print(tenki_data['forecasts'][1]['telop'])
print(tenki_data['forecasts'][1]['temperature']['min']['celsius'])
print(tenki_data['forecasts'][1]['temperature']['max']['celsius'])
