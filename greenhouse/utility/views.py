from django.http import JsonResponse
from django.shortcuts import render

from . import dbhelper

def returnjson(request):
    context = {
        'avg_temp': dbhelper.get_avg('temp').avg_value,
        'avg_air_hum': dbhelper.get_avg('air_hum').avg_value,
        'air_hum_1': dbhelper.get('air_hum',1).value,
        'air_hum_2': dbhelper.get('air_hum',2).value,
        'air_hum_3': dbhelper.get('air_hum',3).value,
        'air_hum_4': dbhelper.get('air_hum',4).value,
        'soil_hum_1': dbhelper.get('soil_hum',1).value,
        'soil_hum_2': dbhelper.get('soil_hum',2).value,
        'soil_hum_3': dbhelper.get('soil_hum',3).value,
        'soil_hum_4': dbhelper.get('soil_hum',4).value,
        'soil_hum_5': dbhelper.get('soil_hum',5).value,
        'soil_hum_6': dbhelper.get('soil_hum',6).value,
        'temp_1': dbhelper.get('temp',1).value,
        'temp_2': dbhelper.get('temp',2).value,
        'temp_3': dbhelper.get('temp',3).value,
        'temp_4': dbhelper.get('temp',4).value,
    }
    return JsonResponse(context)