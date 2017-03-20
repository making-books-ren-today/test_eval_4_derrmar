# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 18:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DerridaWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True)),
                ('short_title', models.CharField(max_length=255)),
                ('full_citation', models.TextField()),
                ('is_primary', models.BooleanField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='References',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('derridawork_page', models.IntegerField()),
                ('derridawork_pageloc', models.CharField(max_length=2)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.Book')),
                ('derridawork', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.DerridaWork')),
            ],
        ),
        migrations.CreateModel(
            name='ReferenceTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notes', models.TextField(blank=True)),
                ('type', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]