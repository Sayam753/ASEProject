import pytest
import clearbit
import requests

clearbit_api_my_key = "sk_bf1dc98c0ebca0d77bca799a3dd9578d"
email_hunter_api_my_key = "e579f150890fafcf58d881a990716d03e28faaa8"

@pytest.mark.parametrize("clearbit_api_key , email_hunter_api_key, domain , extras" , [
    (clearbit_api_my_key,email_hunter_api_my_key,"google.com",None),
    (clearbit_api_my_key,email_hunter_api_my_key,"--","Wrong domain"),
    ("Hello World",email_hunter_api_my_key, "google.com","Wrong key"),
    ("Hello World" ,email_hunter_api_my_key, "google.com","Wrong -both"),
    (clearbit_api_my_key,"ABCs","google.com","Wrong emailHunterkey")
	])
def test_domain(clearbit_api_key , email_hunter_api_key, domain , extras):
	if extras == "Wrong domain" or extras == "Wrong key" or extras == "Wrong -both":
		with pytest.raises(Exception):
			clearbit.key = clearbit_api_key
			company = clearbit.Company.find(domain=domain, stream=True)
	else:
		url = 'https://api.hunter.io/v2/domain-search?domain={}&api_key={}'.format(domain,email_hunter_api_key)
		response = requests.get(url)

		if response.status_code == 401 and extras == "Wrong emailHunterkey":
			print("Invalid API key")
			assert True
		elif response.status_code == 200:	
			json_response = response.json()
			assert True	
		else:
			assert False				