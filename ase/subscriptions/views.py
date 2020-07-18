import stripe
from django.shortcuts import render
from django.urls import reverse
from django.conf import settings


def subscribe(request):
    stripe.api_key = settings.STRIPE_PRIVATE_KEY

    session = stripe.checkout.Session.create(
                    payment_method_types = ['card'],
                    line_items = [{
                        'price' : 'price_1H60pwI24oCI0OTByU54LFUB',
                        'quantity' : 1,
                    }],
                    mode = 'payment',
                    success_url = request.build_absolute_uri(reverse('home')) + '?session_id={CHECKOUT_SESSION_ID}',
                    cancel_url = request.build_absolute_uri(reverse('subscribe')),
    )
    context = {
        'session_id' : session.id,
        'strip_public_key' : settings.STRIPE_PUBLIC_KEY
    }

    return render(request, 'subscriptions/subscription.html', context)
