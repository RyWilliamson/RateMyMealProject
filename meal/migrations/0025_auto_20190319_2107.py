# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 21:07
from __future__ import unicode_literals

from django.db import migrations, models
import meal.models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0024_merge_20190319_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to=meal.models._get_upload_path),
        ),
    ]
