from django.contrib.auth import get_user_model
from django.db import models
from djmoney.models.fields import MoneyField

User = get_user_model()


class Ads(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    price = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency='USD',
        null=True
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name='Автор'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name="category",
        verbose_name='Категория'
    )
    sell_rent = models.ForeignKey(
        'SellRent',
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name='Группа'
    )


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'


class Photo(models.Model):
    image = models.ImageField(upload_to='photos/%Y/%m/%d')
    ads = models.ForeignKey(
        Ads,
        null=True,
        related_name='photos',
        on_delete=models.SET_NULL,
        verbose_name='Фото'
    )


class Location(models.Model):
    country = models.ForeignKey(
        'cities_light.Country',
        null=True,
        on_delete=models.SET_NULL,
        related_name='country',
        verbose_name='Страна'
    )
    city = models.ForeignKey(
        'cities_light.City',
        null=True,
        on_delete=models.SET_NULL,
        related_name='city',
        verbose_name='Город'
    )
    city_slug = models.SlugField(unique=True, verbose_name='URL city')

    def __str__(self):
        return f'Страна: {self.country}, Город: {self.city}, URL: {self.city_slug}'

    class Meta:
        verbose_name = 'Доступная локация'
        verbose_name_plural = 'Доступные локации'


class SellRent(models.Model):
    title = models.CharField(max_length=200, verbose_name='Продажа/Аренда')

    def __str__(self):
        return self.title

class SuperCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Суперкатегория')


class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Категория')
    cat_slug = models.SlugField(unique=True, verbose_name='URL Category')
    supercategory = models.ForeignKey(
        'SuperCategory',
        on_delete=models.CASCADE,
        related_name="supercategory",
        verbose_name='Суперкатегория'
    )

    def __str__(self):
        return self.title


# class FollowAds(models.Model):
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="user",
#         verbose_name='Пользователь'
#     )
#     ads = models.ForeignKey(
#         Ads,
#         on_delete=models.CASCADE,
#         related_name="ads",
#         verbose_name='Объявления'
#     )
#     def __str__(self):
#         return f'User:{self.user}, ads: {self.ads}'
#
#     class Meta:
#         verbose_name = 'Избранное объявление'
#         verbose_name_plural = 'Избранные объявления'
#         unique_together = ['user', 'ads']
#
#
# class FollowAuthors(models.Model):
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="user",
#         verbose_name='Пользователь'
#     )
#     seller = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name="seller",
#         verbose_name='Продавец'
#     )
#     def __str__(self):
#         return f'User:{self.user}, seller: {self.seller}'
#
#     class Meta:
#         verbose_name = 'Избранный продавец'
#         verbose_name_plural = 'Избранные продавцы'
#         unique_together = ['user', 'seller']