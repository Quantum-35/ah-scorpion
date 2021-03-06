# Generated by Django 2.0.6 on 2018-08-14 18:50

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,
                                        serialize=False, verbose_name='ID')),
                ('slug',
                 models.CharField(blank=True, max_length=200, null=True,
                                  unique=True)),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('description', models.CharField(max_length=100)),
                ('images', django.contrib.postgres.fields.ArrayField(
                    base_field=models.CharField(blank=True, max_length=1000),
                    blank=True, null=True, size=20)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('tagList', django.contrib.postgres.fields.ArrayField(
                    base_field=models.CharField(max_length=200), blank=True,
                    null=True, size=None)),
                ('author', models.ForeignKey(db_column='author',
                                             on_delete=django.db.models
                                             .deletion.CASCADE,
                                             to=settings.AUTH_USER_MODEL)),
                ('dislikes',
                 models.ManyToManyField(blank=True, related_name='dislikes',
                                        to=settings.AUTH_USER_MODEL)),
                ('favorited',
                 models.ManyToManyField(blank=True, related_name='favorited',
                                        to=settings.AUTH_USER_MODEL)),
                ('likes',
                 models.ManyToManyField(blank=True, related_name='likes',
                                        to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('title',),
            },
        ),
    ]
