# Generated by Django 2.2 on 2019-04-15 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reservation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationinfo',
            name='dateTime',
            field=models.DateTimeField(null=True),
        ),
    ]
