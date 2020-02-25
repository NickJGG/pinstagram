# Generated by Django 2.0 on 2017-12-14 04:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_auto_20171213_2100'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='userfollowing',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='userfollowing',
            name='following',
        ),
        migrations.RemoveField(
            model_name='userfollowing',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='userlikes',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='userlikes',
            name='liked_post',
        ),
        migrations.RemoveField(
            model_name='userlikes',
            name='user',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='following',
            field=models.ManyToManyField(related_name='user_following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='liked_posts',
            field=models.ManyToManyField(to='main.Post'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='user', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='UserFollowing',
        ),
        migrations.DeleteModel(
            name='UserLikes',
        ),
    ]
