# Generated by Django 2.0 on 2017-12-18 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0017_auto_20171217_1941'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='pin',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='pin',
            name='post',
        ),
        migrations.RemoveField(
            model_name='pin',
            name='user',
        ),
        migrations.DeleteModel(
            name='Pin',
        ),
    ]
