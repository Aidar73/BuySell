from django.contrib import admin
from django.urls import path, include

from ads import views
from ads.views import index

urlpatterns = [
    path('', index, name="index"),
    path('<slug:city_slug>/<slug:cat_slug>/<int:ads_id>/', views.ads_view, name='ads_view'),
]
