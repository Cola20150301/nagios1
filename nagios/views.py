# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
import json
# Create your views here.
from common.mymako import render_mako_context
from views_main import Nagios
from fetch_nagios import FetchNagios


def home(request):
    """
    首页
    """
    data = FetchNagios().get_host()
    return render(request, 'nagios/home.html', data)


def get_host(request):
    res = Nagios().get_host_with_nagios()
    return HttpResponse(res)


def add_host(request):
    if request.method == 'POST':
        request = request.POST.copy()
        print request
        res = Nagios().add_host_with_nagios(request)

        return HttpResponse(json.dumps(res))


def del_host(request):
    if request.method == 'POST':
        print 1
        request = request.POST.copy()
        res = Nagios().del_host_with_nagios(request)
        return HttpResponse(json.dumps(res))
