from django.contrib import admin

from subscriptions.models import Subscription, Plan

admin.site.register(Subscription)
admin.site.register(Plan)
