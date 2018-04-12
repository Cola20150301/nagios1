#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/4/9 15:20
# @Author  : Cola
# @Site    :
# @File    : http.py
# @Software: PyCharm
import platform

import requests
from requests.auth import AuthBase
from settings import connection_pool, connection_retries, connection_timeout

_sys_info = '{0}; {1}'.format(platform.system(), platform.machine())
_python_ver = platform.python_version()

USER_AGENT = 'bkpaas/ {0};  Python/{1}'.format(_sys_info, _python_ver)

SESSION = None
HEADERS = {'User-Agent': USER_AGENT}


def __return_wrapper(resp):
    if resp.status_code != 200 or resp.headers.get('X-Reqid') is None:
        return None, ResponseInfo(resp)
    try:
        ret = resp.json() if resp.text != '' else {}
    except:
        ret = {}
    return ret, ResponseInfo(resp)


def _init():
    session = requests.Session()
    adapter = requests.adapters.HTTPAdapter(
        pool_connections=connection_pool, pool_maxsize=connection_pool, max_retries=connection_timeout)
    session.mount('http://', adapter)
    global SESSION
    SESSION = session


def _get(url, params, auth):
    try:
        r = requests.get(
            url, params=params, auth=auth,timeout=connection_timeout, headers=HEADERS)
    except Exception as e:
        return None, ResponseInfo(None, e)


def _post(url, data, files, auth):
    if SESSION is None:
        _init()
    HEADERS['Content-Type'] = 'application/json'
    try:
        r = SESSION.post(
            url, data=data, files=files, auth=auth, timeout=connection_timeout)
    except Exception as e:
        return None, ResponseInfo(None, e)
    return __return_wrapper(r)

