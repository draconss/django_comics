# Generated by Django 2.1.8 on 2019-04-17 13:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20190412_1520'),
    ]

    operations = [
        migrations.AddField(
            model_name='glava',
            name='numver',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='coments',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 17, 16, 26, 9, 401289), verbose_name='Дата комментария'),
        ),
    ]
