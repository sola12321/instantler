# Generated by Django 2.2 on 2019-04-13 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Restaurant', '0008_restaurant_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='rating',
            field=models.IntegerField(default=1),
        ),
    ]