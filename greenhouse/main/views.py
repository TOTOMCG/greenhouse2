from django.shortcuts import render

from records_manager.models import AvgRecord


def returnmain(request):
    one_data = AvgRecord.objects.latest('datetime')  # 1 will return the first item change it depending on the data you want
    context = {
        'one_data': one_data,
    }
    return render(request, 'main/main.html', context)
