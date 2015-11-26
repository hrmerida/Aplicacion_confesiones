# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='confesiones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('Nombre_confesion', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('tag', models.ForeignKey(to='actividades.categoria')),
            ],
        ),
    ]
