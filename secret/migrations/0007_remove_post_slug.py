# Generated by Django 2.0 on 2018-01-12 01:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secret', '0006_post_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
    ]
