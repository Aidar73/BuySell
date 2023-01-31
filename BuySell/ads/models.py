from django.contrib.auth import get_user_model
from django.db import models
from djmoney.models.fields import MoneyField

User = get_user_model()


class Ads(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    price = MoneyField(
        max_digits=14,
        decimal_places=2,
        default_currency='USD',
        null=True,
        verbose_name='Цена'
    )
    sell_rent = models.ForeignKey(
        'SellRent',
        on_delete=models.CASCADE,
        related_name="ads",
        verbose_name='Группа'
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        related_name="ads",
        verbose_name='Категория'
    )
    city = models.ForeignKey(
        'City',
        on_delete=models.CASCADE,
        related_name="ads",
        verbose_name='Город'
    )
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="ads",
        verbose_name='Автор'
    )
    time_created = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)


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


class Country(models.Model):
    name = models.CharField(max_length=200, verbose_name='Страна')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация - Страна'
        verbose_name_plural = 'Локация - Страны'

class City(models.Model):
    name = models.CharField(max_length=200, verbose_name='Город')
    city_slug = models.SlugField(unique=True, verbose_name='URL Category')
    country = models.ForeignKey(
        'Country',
        on_delete=models.CASCADE,
        related_name="ads",
        verbose_name='Страна'
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Локация - Город'
        verbose_name_plural = 'Локация - Города'


class SellRent(models.Model):
    title = models.CharField(max_length=200, verbose_name='Продажа/Аренда')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продажа/Аренда'
        verbose_name_plural = 'Продажа/Аренда'

class SuperCategory(models.Model):
    title = models.CharField(max_length=200, verbose_name='Суперкатегория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Каталог - суперкатегории'
        verbose_name_plural = 'Каталог - суперкатегории'

class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name='Категория')
    cat_slug = models.SlugField(unique=True, verbose_name='URL Category')
    supercategory = models.ForeignKey(
        'SuperCategory',
        on_delete=models.CASCADE,
        related_name="ads",
        verbose_name='Суперкатегория'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Каталог - категории'
        verbose_name_plural = 'Каталог - категории'

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