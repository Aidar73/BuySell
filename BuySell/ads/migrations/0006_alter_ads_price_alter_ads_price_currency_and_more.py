# Generated by Django 4.1 on 2023-02-04 07:54

from django.db import migrations, models
import django.db.models.deletion
import djmoney.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_alter_photo_ads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, default_currency='RUB', max_digits=14, null=True, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='price_currency',
            field=djmoney.models.fields.CurrencyField(choices=[('USD', 'Долларов'), ('GEL', 'Лари'), ('RUB', 'Рублей')], default='RUB', editable=False, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='ads',
            name='sell_rent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ads', to='ads.sellrent', verbose_name='Вид объявления'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='ads',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='ads.ads'),
        ),
    ]