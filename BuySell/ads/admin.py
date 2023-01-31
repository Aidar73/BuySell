from django.contrib import admin
from ads.models import Location, Ads, Category


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Ads)
class AdsAdmin(admin.ModelAdmin):
    list_display = ("title", "text", 'time_created', 'is_published', 'price')
    search_fields = ("text",)
    list_filter = ("time_created",)
    empty_value_display = "-пусто-"


@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ("supercategory", "title", "cat_slug")
    search_fields = ("title",)
    empty_value_display = "-пусто-"
