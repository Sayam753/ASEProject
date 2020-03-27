from .config import *
import shodan
import time


def get_device(device_name):
    response = None
    try:
        api = shodan.Shodan(shodan_api_key)
        results = api.search(device_name)
        time.sleep(5)
        response = results
    except shodan.APIError as e:
        response = {'error': e}
    finally:
        return response
