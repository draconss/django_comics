# Generated by Django 2.2 on 2019-04-12 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20190412_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='datas',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='manga',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
