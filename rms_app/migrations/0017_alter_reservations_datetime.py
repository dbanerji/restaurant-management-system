# Generated by Django 4.2.8 on 2024-02-01 01:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms_app', '0016_oneseater_booked_timeslots_twoseater_booked_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 1, 1, 22, 22, 297221)),
        ),
    ]