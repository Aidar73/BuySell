from django.contrib import admin
from django.urls import path, include

from ads import views
from ads.views import index

urlpatterns = [
    path('', index, name="index"),
    path('new/', views.ads_new, name="ads_new"),
    path('<slug:city_slug>/<slug:cat_slug>/<int:ads_id>/', views.ads_view, name='ads_view'),
    path('<slug:city_slug>/<slug:cat_slug>/<int:ads_id>/edit/', views.ads_edit, name='ads_edit'),
    path('<slug:city_slug>/<slug:cat_slug>/<int:ads_id>/delete/', views.ads_delete, name='ads_delete'),
    path('<str:username>/', views.profile, name='profile'),
]
