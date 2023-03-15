from django.shortcuts import render
from utility import dbhelper, http_request



# Return main .html template
def returnmain(request):
    if request.method == 'POST':
        if request.POST.get('type') == 'checkbox':
            s = request.POST.get('name').split('-')
            http_request.patch(s[0],s[1],1 if request.POST.get('value') == 'true' else 0)
        else:
            dbhelper.update_setting('frequency', request.POST.get('frequency'))
            dbhelper.update_setting('min_temp', request.POST.get('min_temp'))
            dbhelper.update_setting('max_air_hum', request.POST.get('max_air_hum'))
            dbhelper.update_setting('max_soil_hum', request.POST.get('max_soil_hum'))
            dbhelper.update_setting('token', request.POST.get('token'))

    context = {
        'frequency': dbhelper.get_setting('frequency').value,
        'min_temp': dbhelper.get_setting('min_temp').value,
        'max_air_hum': dbhelper.get_setting('max_air_hum').value,
        'max_soil_hum': dbhelper.get_setting('max_soil_hum').value,
        'token': dbhelper.get_setting('token').value,
    }
    return render(request, 'main/index.html', context)
