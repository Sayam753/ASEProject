import pytest
import shodan

my_key = "M3ErsJ85A8xPigPvejyI4fMJVHIu8swN"

@pytest.mark.parametrize("key , device_name, extras" , [
   (my_key,"webcam",None),
    ("qw","webcam" , "wrong key"),
    (my_key , "a" , "Wierd device name"),
	])
def test_device(key,device_name,extras):
	if extras == "wrong key":	
		with pytest.raises(shodan.APIError):
			api = shodan.Shodan(key)
			results = api.search(device_name)
	elif extras == "Wierd device name":
		api = shodan.Shodan(key)
		results = api.search(device_name)	
		assert results["total"] == 0

	else:
		api = shodan.Shodan(key)
		results = api.search(device_name)
		assert True		
