# Generated by Django 2.2 on 2019-04-10 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190409_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glava',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='glava', to='main.Manga'),
        ),
    ]