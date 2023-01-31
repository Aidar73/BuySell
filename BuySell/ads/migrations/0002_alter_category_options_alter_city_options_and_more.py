# Generated by Django 4.1 on 2023-01-31 18:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Каталог - категории', 'verbose_name_plural': 'Каталог - категории'},
        ),
        migrations.AlterModelOptions(
            name='city',
            options={'verbose_name': 'Локация - Город', 'verbose_name_plural': 'Локация - Города'},
        ),
        migrations.AlterModelOptions(
            name='country',
            options={'verbose_name': 'Локация - Страна', 'verbose_name_plural': 'Локация - Страны'},
        ),
        migrations.AlterModelOptions(
            name='sellrent',
            options={'verbose_name': 'Продажа/Аренда', 'verbose_name_plural': 'Продажа/Аренда'},
        ),
        migrations.AlterModelOptions(
            name='supercategory',
            options={'verbose_name': 'Каталог - суперкатегории', 'verbose_name_plural': 'Каталог - суперкатегории'},
        ),
        migrations.RenameField(
            model_name='city',
            old_name='supercategory',
            new_name='country',
        ),
    ]