from django.contrib import admin
from ads.models import *


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ("title", "text", 'time_created', 'is_published', 'price')
    search_fields = ("text",)
    list_filter = ("time_created",)
    empty_value_display = "-пусто-"


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "city_slug", 'country')
    search_fields = ("name",)
    list_filter = ("country",)
    prepopulated_fields = {'city_slug': ('name',),}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "cat_slug", 'supercategory')
    search_fields = ("title",)
    list_filter = ("supercategory",)
    prepopulated_fields = {'cat_slug': ('title',),}


admin.site.register(Country)
admin.site.register(SellRent)
admin.site.register(SuperCategory)
