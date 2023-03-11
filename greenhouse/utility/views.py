from django.http import HttpResponse
from django.shortcuts import render

from . import dbhelper


def returnvalue(request, type, id):
    if id == 'avg':
        return HttpResponse(dbhelper.get_avg(type).avg_value)
    else:
        return HttpResponse(dbhelper.get(type, id).value)


def returnchart(request):
    return render(request, 'layout/charts_layout.html', context=dbhelper.get_table('avg_air_hum'))