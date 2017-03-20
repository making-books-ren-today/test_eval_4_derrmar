# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 17:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_allow_neg_years_bc'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='has_dedication',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='has_insertions',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='is_translation',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_extant',
            field=models.BooleanField(default=False, help_text='Extant in PUL JD'),
        ),
        migrations.AlterField(
            model_name='book',
            name='uri',
            field=models.URLField(blank=True, help_text='Finding Aid URL', null=True),
        ),
    ]