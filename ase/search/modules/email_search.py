from .config import *
import requests
import json


def fetch_email(email_id):
    url = 'https://api.fullcontact.com/v3/person.enrich'
    headers = {"Authorization": f"Bearer {fullcontact_api_key}"}
    data = json.dumps({"email": email_id})
    response = requests.post(url, data=data, headers=headers)

    return response.json()
