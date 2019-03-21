# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-19 15:58
from __future__ import unicode_literals

from django.db import migrations, models
import meal.models


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0015_delete_recipeprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to=meal.models._get_upload_path),
        ),
    ]