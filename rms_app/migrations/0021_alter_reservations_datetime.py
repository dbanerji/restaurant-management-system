# Generated by Django 4.2.8 on 2024-02-25 22:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rms_app', '0020_alter_reservations_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 2, 25, 22, 33, 45, 718800, tzinfo=datetime.timezone.utc)),
        ),
    ]