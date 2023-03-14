from django.shortcuts import render
from utility import dbhelper


# Return main .html template
def returnmain(request):
    # context = {
    #     'token': dbhelper.get_setting('token').value,
    #     'frequency': dbhelper.get_setting('frequency').value,
    #     'min_temp': dbhelper.get_setting('min_temp').value,
    #     'max_air_hum': dbhelper.get_setting('max_air_hum').value,
    #     'max_soil_hum': dbhelper.get_setting('max_soil_hum').value,
    # }
    # if request.method == 'POST':
    #     dbhelper.update_setting('token', request.POST.get('token'))
    if request.method == 'POST':
        # dbhelper.update_setting('token', request.POST.get('token'))
        print(request.POST.get('frequency'))
        print(request.POST.get('min_temp'))
        print(request.POST.get('max_air_hum'))
        print(request.POST.get('max_soil_hum'))
        print(request.POST.get('token'))
    return render(request, 'main/index.html')
