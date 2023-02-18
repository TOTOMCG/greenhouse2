from django.shortcuts import render

from records_manager import dbhelper



def returnmain(request):
    context = {
        'avg_temp': dbhelper.get_avg('temp'),
        'avg_air_hum': dbhelper.get_avg('air_hum'),
        'air_hum_1': dbhelper.get('air_hum',1),
        'air_hum_2': dbhelper.get('air_hum',2),
        'air_hum_3': dbhelper.get('air_hum',3),
        'air_hum_4': dbhelper.get('air_hum',4),
        'soil_hum_1': dbhelper.get('soil_hum',1),
        'soil_hum_2': dbhelper.get('soil_hum',2),
        'soil_hum_3': dbhelper.get('soil_hum',3),
        'soil_hum_4': dbhelper.get('soil_hum',4),
        'soil_hum_5': dbhelper.get('soil_hum',5),
        'soil_hum_6': dbhelper.get('soil_hum',6),
        'temp_1': dbhelper.get('temp',1),
        'temp_2': dbhelper.get('temp',2),
        'temp_3': dbhelper.get('temp',3),
        'temp_4': dbhelper.get('temp',4),
    }
    return render(request, 'main/main.html', context)
