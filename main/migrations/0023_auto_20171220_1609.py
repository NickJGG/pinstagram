# Generated by Django 2.0 on 2017-12-20 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_auto_20171219_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='picture',
            new_name='image',
        ),
    ]
