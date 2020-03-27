from .config import *
import shodan


def ip_details(ip):
    response = None
    try:
        api = shodan.Shodan(shodan_api_key)
        host = api.host(ip)
        response = host
    except shodan.APIError as e:
        response = {'error': e}
    finally:
        return response

