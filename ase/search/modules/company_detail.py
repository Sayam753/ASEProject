from .config import *
import clearbit
import requests
clearbit.key = clearbit_api_key


def get_company_detail(domain):
    response = None
    try:
        company = clearbit.Company.find(domain=domain, stream=True)
    except Exception as e:
        response = {'error': e}
    else:
        company_details = None
        if company is not None:
            company_details = dict(company)

        # Extracting emails
        url = f'https://api.hunter.io/v2/domain-search?domain={domain}&api_key={email_hunter_api_key}'
        response = requests.get(url)
        json_response = response.json()
        if response.ok:
            company_details['Extracted Emails'] = json_response
        else:
            company_details['Error for Email Extraction'] = json_response
        response = company_details
    finally:
        return response
