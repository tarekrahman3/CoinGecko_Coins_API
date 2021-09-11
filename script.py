import json
import requests
import time
import pandas as pd
from load_json import load_json

def get_address(dict:dict):
	try:
		return dict['platforms']['polygon-pos']
	except:
		return None

def get_market_cap(dict:dict):
	try:
		return dict["market_data"]['market_cap']['usd']
	except:
		return None

def get_total_volume(dict:dict):
	try:
		return dict['market_data']['total_volume']['usd']
	except:
		return None

def get_website(dict:dict):
	try:
		return dict['links']['homepage'][0]
	except:
		return None

def get_all_tag(dict:dict):
	try:
		return dict['categories']
	except:
		return None

def get_first_tag(dict:dict):
	try:
		return dict['categories'][0]
	except:
		return None

def get_coinid(dict:dict):
	try:
		return dict['id']
	except:
		return None

def get_symbol(dict:dict):
	try:
		return dict['symbol']
	except:
		return None

def get_name(dict:dict):
	try:
		return dict['name']
	except:
		return None

def json_data():
	return load_json()

def getmetadata(api_key):
	headers = {'accept': 'application/json'}
	baseurl = 'https://api.coingecko.com/api/v3/coins/'
	flags = '?localization=false&community_data=false&developer_data=false&sparkline=false'
	response = requests.get(f'{baseurl}/{api_key}{flags}', headers = headers)
	return response
output=[]
coins = json_data()

try:
	i=1
	for each_coin in coins:
		coin_name = get_name(each_coin)
		coin_id = get_coinid(each_coin)
		coin_symbol = get_symbol(each_coin)
		response = getmetadata(coin_id)
		response_status = response.status_code
		try:
			response_json = response.json()
		except:
			response_json = None
		response.close()
		address = get_address(response_json)
		print(f"{i} | {response_status} | {coin_name} | {address}")
		data = {
		'coin_name':coin_name,
		'coin_id': coin_id,
		'coin_symbol':coin_symbol,
		'response_status':response_status,
		'polygon_address': address,
		'market_cap':get_market_cap(response_json),
		'total_volume':get_total_volume(response_json),
		'website': get_website(response_json),
		'tag_number_one' : get_first_tag(response_json),
		'all_atags' : get_all_tag(response_json)
		}
		output.append(data)
		time.sleep(0.5)
		i+=1
finally:
	pd.DataFrame(output).to_csv('output.csv')