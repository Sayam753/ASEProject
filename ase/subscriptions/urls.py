from django.urls import path, include

from subscriptions.views import subscribe, checkout

urlpatterns = [
    path('', subscribe, name='subscribe'),
    path('checkout/', checkout, name='checkout')
]
