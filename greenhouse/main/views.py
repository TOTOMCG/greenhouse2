from django.shortcuts import render
from utility import dbhelper, http_request
import time


# Return main .html template
def returnmain(request):
    if request.method == 'POST':
        if request.POST.get('type') == 'checkbox':
            print(request.POST)
            s = request.POST.get('name').split('-')
            http_request.patch(s[0], s[1], 1 if request.POST.get('value') == 'true' else 0)
        else:
            if request.POST.get('min_temp', False):
                dbhelper.update_setting('min_temp', request.POST.get('min_temp'))
                dbhelper.update_setting('max_air_hum', request.POST.get('max_air_hum'))
                dbhelper.update_setting('max_soil_hum', request.POST.get('max_soil_hum'))
                dbhelper.update_setting('token', request.POST.get('token'))
            else:
                s = request.POST.get('deviceselected').split('-')
                dbhelper.add(s[0], s[1], time.strftime("%H:%M:%S %d-%m-%Y",
                                                       time.strptime(request.POST.get('datetime') + ':00',
                                                                     "%Y-%m-%dT%H:%M:%S")), request.POST.get('value'))
            print(request.POST)
    context = {
        'frequency': dbhelper.get_setting('frequency').value,
        'min_temp': dbhelper.get_setting('min_temp').value,
        'max_air_hum': dbhelper.get_setting('max_air_hum').value,
        'max_soil_hum': dbhelper.get_setting('max_soil_hum').value,
        'token': dbhelper.get_setting('token').value,
        'watering_1': True if dbhelper.get_last('watering', 1) == 1 else False,
        'watering_2': True if dbhelper.get_last('watering', 2) == 1 else False,
        'watering_3': True if dbhelper.get_last('watering', 3) == 1 else False,
        'watering_4': True if dbhelper.get_last('watering', 4) == 1 else False,
        'watering_5': True if dbhelper.get_last('watering', 5) == 1 else False,
        'watering_6': True if dbhelper.get_last('watering', 6) == 1 else False,
        'total_hum_1': True if dbhelper.get_last('total_hum', 1) == 1 else False,
        'fork_drive_1': True if dbhelper.get_last('fork_drive', 1) == 1 else False,
    }
    return render(request, 'main/index.html', context)
