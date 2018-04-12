#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 15:20
# @Author  : Cola
# @Site    : 
# @File    : views_main.py
# @Software: PyCharm


import requests, json
from settings import APP_ID, APP_TOKEN, BK_PAAS_HOST, NAGIOS_URL, NAGIOS_API_KEY
import models


class Nagios(object):
    def __init__(self):
        pass

    def get_host_with_esb_selfhelp(self):
        url = '%s/api/c/self-service-api/idc/nagios/get_host/' % (BK_PAAS_HOST)
        params = {
            'app_code': APP_ID,
            'app_secret': APP_TOKEN,
            'apikey': API_KEY,
            'username': 'admin'
        }

        r = requests.get(url=url, params=params)
        print r.text
        print r.json()
        if r.status_code == 200:
            models.Host.objects.all().delete()
            models.Host.objects.bulk_create(r.json()['hostlist']['host'])
            # for i in r.json():
            #     print i
            #     models.Host.objects.update_or_create(instance_id=i['instance_id'],defaults=i)
            return 200
        else:
            print 'nagios get host api failed!'
            return 'nagios get host api failed!'

    def get_host_with_nagios(self):
        url = 'http://%s/nagiosxi/api/v1/objects/host/' % (NAGIOS_URL)
        params = {
            'apikey': NAGIOS_API_KEY,
        }

        r = requests.get(url=url, params=params)
        print r.text
        print r.json()
        if r.status_code == 200:
            models.Host.objects.all().delete()
            host_list = []
            data = r.json()['hostlist']['host']
            for i in data:
                host_list.append(models.Host(
                    # pk=data.index(i),
                    instance_id=i['instance_id'],
                    host_name=i['host_name'],
                    is_active=i['is_active'],
                    config_type=i['config_type'],
                    alias=i['alias'],
                    display_name=i['display_name'],
                    address=i['address'],
                    check_interval=i['check_interval'],
                    retry_interval=i['retry_interval'],
                    max_check_attempts=i['max_check_attempts'],
                    first_notification_delay=i['first_notification_delay'],
                    notification_interval=i['notification_interval'],
                    passive_checks_enabled=i['passive_checks_enabled'],
                    active_checks_enabled=i['active_checks_enabled'],
                    notifications_enabled=i['notifications_enabled'],
                    notes=i['notes'],
                    notes_url=i['notes_url'],
                    action_url=i['action_url'],
                    icon_image=i['icon_image'],
                    icon_image_alt=i['icon_image_alt'],
                    statusmap_image=i['statusmap_image'],
                ))
            print host_list
            models.Host.objects.bulk_create(host_list)
            # for i in r.json()['hostlist']['host']:
            #     print i
            #     i.pop('@attributes')
            #     models.Host.objects.update_or_create(address=i['address'], defaults=i)
            return 200
        else:
            print 'nagios get host api failed!'
            return 'nagios get host api failed!'

    def add_host_with_nagios(self, params):
        url = 'http://%s/nagiosxi/api/v1/config/host?apikey=%s' % (NAGIOS_URL, NAGIOS_API_KEY)
        data = {
            'host_name': params['host_name'],
            'address': params['address'],
            'max_check_attempts': params['max_check_attempts'],
            'check_period': params['check_period'],
            'contact_groups': params['contact_groups'],
            'notification_interval': params['notification_interval'],
            'notification_period': params['notification_period'],
            'applyconfig': 1
        }
        r = requests.post(url=url, data=data)
        return r.json()

    def del_host_with_nagios(self, params):
        url = 'http://%s/nagiosxi/api/v1/config/host?apikey=%s&host_name=%s&applyconfig=1' % (
        NAGIOS_URL, NAGIOS_API_KEY, params['host_name'])

        # print url,data
        r = requests.delete(url=url)
        # print r.text
        # print r.json()
        return r.json()
