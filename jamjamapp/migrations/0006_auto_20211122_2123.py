# Generated by Django 3.2.6 on 2021-11-22 12:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jamjamapp', '0005_alter_blog_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='favorite_post', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blog',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like_post', to=settings.AUTH_USER_MODEL),
        ),
    ]
