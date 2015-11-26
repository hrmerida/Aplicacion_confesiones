# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0008_producto_precio'),
    ]

    operations = [
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='confesiones',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('Nombre_confesion', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('tag', models.ForeignKey(to='actividades.categoria')),
            ],
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='comentario',
            name='producto',
        ),
        migrations.DeleteModel(
            name='comentario',
        ),
        migrations.DeleteModel(
            name='producto',
        ),
    ]
