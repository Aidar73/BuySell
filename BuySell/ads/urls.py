from django.contrib import admin
from django.urls import path, include

from ads.views import index

urlpatterns = [
    path('', index),
]
