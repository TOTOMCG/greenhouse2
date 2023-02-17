from django.shortcuts import render

from records_manager import dbhelper



def returnmain(request):
    context = {
        'avg_temp': dbhelper.get_avg('temp'),
        'avg_hum': dbhelper.get_avg('hum'),
        'hum_air_1': dbhelper.get('hum',1),
        'hum_air_2': dbhelper.get('hum',2),
        'hum_air_3': dbhelper.get('hum',3),
        'hum_air_4': dbhelper.get('hum',4),
        'soilhum_1': dbhelper.get('soilhum',1),
        'soilhum_2': dbhelper.get('soilhum',2),
        'soilhum_3': dbhelper.get('soilhum',3),
        'soilhum_4': dbhelper.get('soilhum',4),
        'soilhum_5': dbhelper.get('soilhum',5),
        'soilhum_6': dbhelper.get('soilhum',6),
        'temp_1': dbhelper.get('temp',1),
        'temp_2': dbhelper.get('temp',2),
        'temp_3': dbhelper.get('temp',3),
        'temp_4': dbhelper.get('temp',4),
    }
    return render(request, 'main/main.html', context)
