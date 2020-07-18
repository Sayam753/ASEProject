from django.urls import path, include

from subscriptions.views import subscribe, trial, basic, premium, diamond, stripe_webhook

urlpatterns = [
    path('', subscribe, name='subscribe'),
    path('trial/', trial, name='trial'),
    path('basic/', basic, name='basic'),
    path('premium/', premium, name='premium'),
    path('diamond/', diamond, name='diamond'),
    path('stripe_webhook/', stripe_webhook, name='stripe_webhook'),

]
