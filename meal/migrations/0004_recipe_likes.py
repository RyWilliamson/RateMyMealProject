# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-09 11:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0003_remove_userprofile_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
