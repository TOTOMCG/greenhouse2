from django.http import HttpResponse
from django.shortcuts import render

from . import dbhelper


def returnvalue(request, type, id):
    if id == 'avg':
        return HttpResponse(dbhelper.get_last_avg(type).value)
    else:
        return HttpResponse(dbhelper.get_last(type, id).value)


def returnchart(request,type):
    return render(request, 'layout/charts_layout.html', context=dbhelper.get_table(type))