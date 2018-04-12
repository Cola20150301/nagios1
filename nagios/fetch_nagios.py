#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 15:17
# @Author  : Cola
# @Site    : 
# @File    : fetch_nagios.py
# @Software: PyCharm

import models

class FetchNagios(object):
    def get_host(self):
        data_list = []
        account_list = models.Host.objects.all()
        for obj in account_list:
            data = {
                'instance_id': None or str(obj.instance_id.encode('utf8')),
                'host_name': None or str(obj.host_name.encode('utf8')),
                'is_active': None or str(obj.is_active.encode('utf8')),
                'config_type': None or str(obj.config_type.encode('utf8')),
                'alias': None or str(obj.alias.encode('utf8')),
                'display_name': None or str(obj.display_name.encode('utf8')),
                'address': None or str(obj.address),
                'check_interval': None or str(obj.check_interval),
                'retry_interval': None or str(obj.retry_interval),
                'max_check_attempts': None or str(obj.max_check_attempts),
                'first_notification_delay': None or str(obj.first_notification_delay),
                'notification_interval': None or str(obj.notification_interval),
                'passive_checks_enabled': None or str(obj.passive_checks_enabled),
                'active_checks_enabled': None or str(obj.active_checks_enabled),
                'notifications_enabled': None or str(obj.notifications_enabled),
                'notes': None or str(obj.notes),
                'notes_url': None or str(obj.notes_url),
                'action_url': None or str(obj.action_url),
                'icon_image': None or str(obj.icon_image),
                'icon_image_alt': None or str(obj.icon_image_alt),
                'statusmap_image': None or str(obj.statusmap_image),
            }
            data_list.append(data)
        return {'data': data_list}
