import pytest
import requests
import json

my_key = "TZMvcmEC8bahQHlCKWkZ8jzGLs6Fosrn"

@pytest.mark.parametrize("fullcontact_api_key,email_id,extras" , [
   (my_key,"isha.a18@iiits.in",200),
   (my_key,"isha16102000@gmail.com",404),
   ("IshaAggarwal","isha.a18@iiits.in",401),
   ("" , "isha.a18@iiits.in" , 403),  
   (my_key,"abc",400),
   (my_key , 1234, 400) 
	])
def test_email(fullcontact_api_key,email_id,extras):
	url = 'https://api.fullcontact.com/v3/person.enrich'
	headers = {"Authorization": "Bearer {}".format(fullcontact_api_key)}
	data = json.dumps({"email": email_id})
	response = requests.post(url, data=data, headers=headers)
	
	if response.status_code != 200:
		response = response.json()
		if extras == 403:
			assert response['message'] == "Invalid authentication"
		elif extras == 401:
			assert response['message'] == "401: Invalid access token: {}".format(fullcontact_api_key)

		elif extras == 404:
			assert response['message'] == 'Profile not found'
		elif extras == 400:
			assert response['message'] == "Invalid email provided in email section: '{}'".format(email_id)	
	else:
		if response.status_code == 200:
			response = response.json()
			assert True
		else:
			assert False					
