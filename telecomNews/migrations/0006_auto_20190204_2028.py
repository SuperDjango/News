# Generated by Django 2.1.5 on 2019-02-04 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telecomNews', '0005_auto_20190204_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, upload_to='telecomNews/images'),
        ),
    ]
