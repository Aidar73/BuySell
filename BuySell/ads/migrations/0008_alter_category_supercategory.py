# Generated by Django 4.1 on 2023-02-05 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_alter_photo_ads'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='supercategory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='ads.supercategory', verbose_name='Суперкатегория'),
        ),
    ]
