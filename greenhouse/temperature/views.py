from django.shortcuts import render


def returntemperaute(request):
    return render(request, 'temperature/temperature.html')
