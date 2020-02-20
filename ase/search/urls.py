from django.urls import path, re_path
from search import views


urlpatterns = [
	path('btc-block/', views.get_btc_block, name='get-btc-block'),
	path('btc-date/', views.get_btc_date, name='get-btc-date'),
	# re_path('^btc-date/(?P<date>\d+)/$', views.find_btc_date, name='find-btc-date'),
]
