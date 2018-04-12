# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='address',
            field=models.CharField(unique=True, max_length=60, verbose_name='IP\u5730\u5740'),
        ),
    ]
