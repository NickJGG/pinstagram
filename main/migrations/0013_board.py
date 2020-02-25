# Generated by Django 2.0 on 2017-12-17 18:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('main', '0012_auto_20171215_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=20)),
                ('pins', models.ManyToManyField(to='main.Post')),
            ],
        ),
    ]
