# Generated by Django 4.2.8 on 2024-01-31 17:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms_app', '0009_alter_reservations_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 31, 17, 48, 54, 197042)),
        ),
    ]
