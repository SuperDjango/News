# Generated by Django 2.1.5 on 2019-02-04 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telecomNews', '0002_auto_20190129_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
    ]
