# Generated by Django 3.2.6 on 2021-09-25 21:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210925_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatoredge',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 25, 16, 20, 28, 712124)),
        ),
        migrations.AlterField(
            model_name='upload',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 25, 16, 20, 28, 710623)),
        ),
    ]
