# Generated by Django 2.0 on 2017-12-19 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20171219_1113'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='board',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='board',
            name='post',
        ),
        migrations.RemoveField(
            model_name='board',
            name='user',
        ),
        migrations.DeleteModel(
            name='Board',
        ),
    ]
