# Generated by Django 4.1 on 2023-02-04 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_alter_ads_price_alter_ads_price_currency_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='ads',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ads.ads'),
        ),
    ]