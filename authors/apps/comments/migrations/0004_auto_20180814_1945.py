# Generated by Django 2.0.6 on 2018-08-14 19:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0003_auto_20180809_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='dislikes',
            field=models.ManyToManyField(
                blank=True,
                related_name='comment_dislikes',
                to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(
                blank=True,
                related_name='comment_likes',
                to=settings.AUTH_USER_MODEL),
        ),
    ]