# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-16 06:07
from __future__ import unicode_literals

import art.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('art', '0003_auto_20170516_0819'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='css_background_color_menu',
            field=models.CharField(blank=True, help_text='Use hex color or colors like blue etc', max_length=50, null=True, validators=[art.models.validate_hex_color], verbose_name='Background Color'),
        ),
        migrations.AddField(
            model_name='art',
            name='href_color',
            field=models.CharField(blank=True, help_text='Use hex color or colors like blue etc', max_length=50, null=True, validators=[art.models.validate_hex_color], verbose_name='Background Color'),
        ),
    ]