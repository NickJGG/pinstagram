# Generated by Django 2.0 on 2017-12-15 20:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20171214_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='dob',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]