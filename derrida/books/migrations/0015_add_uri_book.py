# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0014_add_flags_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='uri',
            field=models.URLField(blank=True, null=True),
        ),
    ]