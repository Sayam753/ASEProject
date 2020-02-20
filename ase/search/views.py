from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from .utils import format_dict
from . import forms

# Create your views here.
def get_btc_block(request):
    if request.method=='GET':
        url="https://chain.api.btc.com/v3/block/latest"

        try:
            response = requests.get(url)
        except requests.exceptions.ConnectionError:
            pass
            # print("Unable to fetch data! Check your internet connection.")
        except Exception as e:
            pass
            # print(e)
        else:
            if response.status_code == 403:
                # print('Forbidden Access. Try after some time.')
                return

            response = response.json()

            if response['err_no'] == 0:
                data = response['data']
                # if data:
                #     if isinstance(data, list):
                #         for item in data:
                #             format_dict(item)
                #             # print()
                #     else:
                #         format_dict(data)
                # else:
                #     pass
                    # print('No related information found.')

            else:
                # print(f"Error Number:: {response['err_no']}")
                # print(f"Error Message:: {response['err_msg']}")
                url="https://chain.api.btc.com/v3/block/latest"

    return render(request, 'search/random.html', {'response':response})

def get_btc_date(request):
    if request.method=='POST':
        form=forms.SearchForm(request.POST)
        if form.is_valid():
            form.save()
            target=form.cleaned_data.get('target')
            return redirect(f'btc-date/{target}')

    else:
        form=forms.SearchForm()
        print(form)

    return render(request,'search/searchform.html',{'form':form})
