from django.urls import path, include

from subscriptions.views import subscribe

urlpatterns = [
    path('', subscribe, name='subscribe')
]
