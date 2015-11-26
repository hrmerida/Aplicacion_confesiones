# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0002_auto_20151120_0953'),
    ]

    operations = [
        migrations.CreateModel(
            name='confesioness',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('producto', models.ForeignKey(to='actividades.producto')),
            ],
        ),
        migrations.RemoveField(
            model_name='confesiones',
            name='producto',
        ),
        migrations.DeleteModel(
            name='confesiones',
        ),
    ]
