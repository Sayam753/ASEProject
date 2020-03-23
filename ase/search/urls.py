from django.urls import path
from .views import home, query


urlpatterns = [
    path('', home, name='home'),
    path('search/<str:argument>', query, name='search')
]

