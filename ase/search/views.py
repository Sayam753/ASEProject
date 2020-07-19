from django.shortcuts import render, redirect
from django.http import HttpResponse
from .modules import *
from .forms import SearchForm
from blockcypher import get_blockchain_overview, get_address_details, get_block_overview
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from subscriptions.models import Subscription

def home(request):
    return render(request, 'search/osint.html')

@login_required(redirect_field_name='next', login_url=reverse_lazy('login'))
def query(request, argument):
    """
    query view returns the result of the user query about btc, domain, email, device, ip etc.
    """

    user = request.user
    if user.subscribed:
        if request.method == "POST":
            form = SearchForm(request.POST)
            if form.is_valid():
                arg = form.cleaned_data.get('query')
                response = None
                if argument == "btc_block_overview":
                    try:
                        response = get_block_overview(arg)
                    except AssertionError:
                        response = {'error': 'invalid input'}
                elif argument == "btc_address":
                    try:
                        response = get_address_details(arg)
                    except AssertionError:
                        response = {'error': 'invalid input'}
                elif argument == "domain":
                    response = get_company_detail(arg)
                elif argument == "email":
                    response = fetch_email(arg)
                elif argument == "device":
                    response = get_device(arg)
                elif argument == "ip":
                    response = ip_details(arg)

                #decrement the remaining searches by one
                subscription = Subscription.objects.filter(user=user).order_by('-id').first()
                subscription.decrement_searches
                if not subscription.has_searches_left:
                    subscription.change_to_deactivated
                    user.subscribed=False
                    user.save()
                subscription.save()
                return render(request, 'search/random.html', {'response': response})

        else:
            if argument == "btc_block":
                response = get_blockchain_overview()

                #decrement the remaining searches by one
                subscription = Subscription.objects.filter(user=user).order_by('-id').first()
                subscription.decrement_searches
                if not subscription.has_searches_left:
                    subscription.change_to_deactivated
                    user.subscribed=False
                    user.save()
                subscription.save()

                return render(request, 'search/random.html', {'response': response})

            form = SearchForm()
        return render(request, 'search/osint.html', {'form': form})

    else:
        return redirect(reverse_lazy('subscribe'))
