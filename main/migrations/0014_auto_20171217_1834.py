# Generated by Django 2.0 on 2017-12-17 23:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_board'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='board',
            name='pins',
        ),
        migrations.RemoveField(
            model_name='board',
            name='user',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
    ]