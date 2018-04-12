# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('instance_id', models.CharField(max_length=60, verbose_name='\u5b9e\u4f8bID')),
                ('host_name', models.CharField(max_length=60, verbose_name='\u4e3b\u673a\u540d')),
                ('is_active', models.CharField(max_length=60)),
                ('config_type', models.CharField(max_length=60)),
                ('alias', models.CharField(max_length=60)),
                ('display_name', models.CharField(max_length=60)),
                ('address', models.CharField(max_length=60, verbose_name='IP\u5730\u5740')),
                ('check_interval', models.CharField(max_length=60)),
                ('retry_interval', models.CharField(max_length=60)),
                ('max_check_attempts', models.CharField(max_length=60)),
                ('first_notification_delay', models.CharField(max_length=60)),
                ('notification_interval', models.CharField(max_length=60)),
                ('passive_checks_enabled', models.CharField(max_length=60)),
                ('active_checks_enabled', models.CharField(max_length=60)),
                ('notifications_enabled', models.CharField(max_length=60)),
                ('notes', models.CharField(max_length=60)),
                ('notes_url', models.CharField(max_length=60)),
                ('action_url', models.CharField(max_length=60)),
                ('icon_image', models.CharField(max_length=60)),
                ('icon_image_alt', models.CharField(max_length=60)),
                ('statusmap_image', models.CharField(max_length=60)),
            ],
            options={
                'verbose_name': 'Nagios\u4e3b\u673a',
                'verbose_name_plural': 'Nagios\u4e3b\u673a',
            },
        ),
    ]
