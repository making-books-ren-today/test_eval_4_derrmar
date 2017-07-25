# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-13 20:43
from __future__ import unicode_literals

import derrida.interventions.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import uuid
from django.core.management import call_command


def load_initial_tags(apps, schema_editor):
    call_command('loaddata', 'initial_tags', app_label='interventions',
                 verbose=0)

class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0003_reference_canvases'),
        ('djiffy', '0002_view_permissions'),
        ('people', '0002_allow_neg_years_bc'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Intervention',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('text', models.TextField(blank=True)),
                ('quote', models.TextField(blank=True)),
                ('uri', models.URLField()),
                ('extra_data', jsonfield.fields.JSONField(default='{}')),
                ('intervention_type', models.CharField(choices=[('A', 'Annotation'), ('I', 'Insertion')], default='A', max_length=2)),
                ('text_translation', models.TextField(blank=True, help_text='Translation of the intervention text (optional)')),
                ('author', models.ForeignKey(blank=True, default=derrida.interventions.models.get_default_intervener, null=True, on_delete=django.db.models.deletion.CASCADE, to='people.Person')),
                ('canvas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djiffy.Canvas')),
                ('quote_language', models.ForeignKey(blank=True, help_text='Language of the anchor text', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='books.Language')),
            ],
            options={
                'permissions': (('view_intervention', 'View intervention'),),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('notes', models.TextField(blank=True)),
                ('applies_to', models.CharField(choices=[('A', 'Annotations only'), ('I', 'Insertions only'), ('AI', 'Both Annotations and Insertions')], default='AI', help_text='Type or types of interventions this tag is applicable to.', max_length=2)),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='intervention',
            name='tags',
            field=models.ManyToManyField(blank=True, help_text='Tags to describe this intervation and its characteristics', to='interventions.Tag'),
        ),
        migrations.AddField(
            model_name='intervention',
            name='text_language',
            field=models.ForeignKey(blank=True, help_text='Language of the intervention text', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='books.Language'),
        ),
        migrations.AddField(
            model_name='intervention',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        # load an initial set of intervention tags
        migrations.RunPython(
            code=load_initial_tags,
            reverse_code=migrations.RunPython.noop,
        ),
    ]