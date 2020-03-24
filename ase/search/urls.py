from django.urls import path
from .views import home, index, query


urlpatterns = [
    path('', home, name='home'),
    path('index', index, name='index'),
    path('search/<str:argument>', query, name='search')
]

