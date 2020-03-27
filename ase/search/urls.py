from django.urls import path
from .views import home, query


urlpatterns = [

    path('<str:argument>', query, name='search'),
]
