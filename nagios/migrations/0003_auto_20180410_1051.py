# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nagios', '0002_auto_20180409_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='address',
            field=models.CharField(max_length=60, verbose_name='IP\u5730\u5740'),
        ),
        migrations.AlterUniqueTogether(
            name='host',
            unique_together=set([('host_name', 'address')]),
        ),
    ]
