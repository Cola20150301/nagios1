#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 15:04
# @Author  : Cola
# @Site    :
# @File    : models.py
# @Software: PyCharm

from django.db import models

# Create your models here.

class Host(models.Model):
    instance_id = models.CharField(u'实例ID', max_length=60)
    host_name = models.CharField(u'主机名', max_length=60)
    is_active = models.CharField(max_length=60)
    config_type = models.CharField(max_length=60)
    alias = models.CharField(max_length=60)
    display_name = models.CharField(max_length=60)
    address = models.CharField(u'IP地址', max_length=60)
    check_interval = models.CharField(max_length=60)
    retry_interval = models.CharField(max_length=60)
    max_check_attempts = models.CharField(max_length=60)
    first_notification_delay = models.CharField(max_length=60)
    notification_interval = models.CharField(max_length=60)
    passive_checks_enabled = models.CharField(max_length=60)
    active_checks_enabled = models.CharField(max_length=60)
    notifications_enabled = models.CharField(max_length=60)
    notes = models.CharField(max_length=60)
    notes_url = models.CharField(max_length=60)
    action_url = models.CharField(max_length=60)
    icon_image = models.CharField(max_length=60)
    icon_image_alt = models.CharField(max_length=60)
    statusmap_image = models.CharField(max_length=60)

    def __unicode__(self):
        return unicode(self.instance_id)

    class Meta:
        verbose_name = u'Nagios主机'
        verbose_name_plural = u"Nagios主机"
        unique_together = ('host_name', 'address')
