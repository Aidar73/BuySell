# Generated by Django 4.1 on 2023-02-02 09:52

import ads.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_ads_price_followsellers_followads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='ads',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ads.ads'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to=ads.models.get_image_filename, verbose_name='Фото'),
        ),
    ]
