# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-03-21 11:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0030_merge_20190320_2039'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='profile_images')),
                ('recipe', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='meal.Recipe')),
            ],
        ),
    ]
