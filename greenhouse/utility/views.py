from django.http import HttpResponse
from django.shortcuts import render

from . import dbhelper


def returnvalue(request, type, id):
    if id == 'avg':
        return HttpResponse(dbhelper.get_avg(type).avg_value)
    else:
        return HttpResponse(dbhelper.get(type, id).value)


def returnchart(request, type):
    return render(request, 'charts/' + type + '.html', context=dbhelper.get_table(type))