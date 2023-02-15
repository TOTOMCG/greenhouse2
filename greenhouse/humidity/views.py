from django.shortcuts import render


def returnhumidity(request):
    return render(request, 'humidity/humidity.html')
