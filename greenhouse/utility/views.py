from django.http import HttpResponse
from django.shortcuts import render

from . import dbhelper

def returnhttp(request,type,id):
    if id == 'avg':
        return HttpResponse(dbhelper.get_avg(type).avg_value)
    else:
        return HttpResponse(dbhelper.get(type,id).value)