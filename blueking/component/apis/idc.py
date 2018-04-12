#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 16:46
# @Author  : Cola
# @Site    : 
# @File    : idc.py
# @Software: PyCharm

from ..base import ComponentAPI


# 系统组件集合类的名称，一般为 Collections + 系统名
class CollectionsIdc(object):

    def __init__(self, client):
        self.client = client

        # get_host为组件名，method为请求组件使用的方法，path为组件路径，组件域名为系统默认域名
        self.create_task = ComponentAPI(
            client=self.client, method='POST', path='/api/c/self-service-api/idc/nagios/get_host/',
            description=u'',
        )