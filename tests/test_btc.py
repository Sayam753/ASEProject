import time 
import json

import pytest
import requests

@pytest.mark.parametrize("url, err_no, extras", [
	("https://chain.api.btc.com/v3/block/latest", 0, None),
	("https://chain.api.btc.com/v3/block/date/2017", 0, None),
	("https://chain.api.btc.com/v3/block/date/20170620", 0, None),
	("https://chain.api.btc.com/v3/block/date/1", 0, "Check empty list"),
	("https://chain.api.btc.com/v3/block/date/1111111", 0, "Check empty list"),
	("https://chain.api.btc.com/v3/block/date/1111111111111", 0, "Check empty list"),
	("https://chain.api.btc.com/v3/block/date/20192040", 2, "Invalid date"),
	("https://chain.api.btc.com/v3/block/date/sayam", 2, "Invalid date"),
	("https://chain.api.btc.com/v3/address/1DST3gm6JthxhuoNKFqXrdpzPFfz1WgHpW", 0, None),
    ("https://chain.api.btc.com/v3/address/1DST3gm6JthxhuoNKFqXrdpzPFfz1WgHp", 0, "Data is none"), 
	("https://chain.api.btc.com/v3/address/1", 2, "Invalid bitcoin"),
	("https://chain.api.btc.com/v3/address/1DST3gm6JthxhuoNKFq", 2, "Invalid bitcoin"),

	#("")
])
def test_btc_block_date_address(url, err_no, extras):
	response = requests.get(url)
	if response.status_code == 500:
		print("We can't do anything! Server side error")
		assert True
	elif response.status_code == 403:
		print("Forbidden access to bitcoin website. Try later or change internet connection.")
		assert True	
	else:
		try:
			response = response.json()	
		except json.decoder.JSONDecodeError:  #(Due to corrupted json response from the server)
			assert True
		else:
			assert response["err_no"] == err_no
			if extras == "Check empty list":
				assert len(response["data"]) == 0
			elif extras == "Invalid date":
				assert response["err_msg"] == "bad params, invalid date: {}".format(url.split('/')[-1])     		
			elif extras == "Data is none":
				assert response["data"] == None
			elif extras == "Invalid Bitcoin":
				assert response["err_msg"] == "bad params: {}".format(url.split('/')[-1])	
			else:
				pass
							