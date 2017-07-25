# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djiffy', '0002_view_permissions'),
        ('books', '0002_instance_digital_edition'),
    ]

    operations = [
        migrations.AddField(
            model_name='reference',
            name='canvases',
            field=models.ManyToManyField(blank=True, help_text="Scanned images from Derrida's Library | ", to='djiffy.Canvas'),
        ),
    ]