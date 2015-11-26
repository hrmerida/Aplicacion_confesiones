# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actividades', '0006_auto_20151120_1018'),
    ]

    operations = [
        migrations.CreateModel(
            name='comentario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion_comentario', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('autor', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('producto', models.ForeignKey(to='actividades.producto')),
            ],
        ),
        migrations.RemoveField(
            model_name='confesione',
            name='autor',
        ),
        migrations.RemoveField(
            model_name='confesione',
            name='producto',
        ),
        migrations.DeleteModel(
            name='confesione',
        ),
    ]
