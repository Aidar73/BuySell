# Generated by Django 4.1 on 2023-02-02 12:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_photo_ads_alter_photo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='ads',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='images', to='ads.ads'),
        ),
    ]
