# Generated by Django 2.0.6 on 2018-08-09 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20180809_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(db_column='article', on_delete=django.db.models.deletion.CASCADE, to='articles.Article'),
        ),
    ]
