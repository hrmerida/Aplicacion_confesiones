# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='categoria',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='confesiones',
            old_name='tag',
            new_name='producto',
        ),
        migrations.RenameField(
            model_name='confesiones',
            old_name='Nombre_confesion',
            new_name='titulo',
        ),
    ]
