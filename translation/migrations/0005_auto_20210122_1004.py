# Generated by Django 3.1.4 on 2021-01-22 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translation', '0004_auto_20210122_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countries',
            name='countrycode',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
