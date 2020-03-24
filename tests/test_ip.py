import pytest
import shodan
import os
my_key = os.environ.get('pass')


@pytest.mark.parametrize("key, ip, extras", [
    (my_key, "45.76.151.11", None),("isha","45.76.151.11","Wrong API"),(my_key, "4346334773","Wrong IP"),("HELLO","23567","Wrong both"),(my_key, "Hello","Wrong IP")
])
def test_ip(key, ip, extras):
    if extras == "Wrong IP" or extras == "Wrong API" or extras == "Wrong both":
        with pytest.raises(shodan.exception.APIError):
            api = shodan.Shodan(key)
            search = api.host(ip)
            """
            print(search)
            print(search.keys())
            print(type(search))
            print(dir(search))
            """
    else:
        api = shodan.Shodan(key)
        search = api.host(ip)    