from django.shortcuts import render


# def returnmain(request):
# return render(request, 'main/main.html')

def returnmainhumidity(request):
    return render(request, 'humidity/humidity.html')

def returnmaintemperature(request):
    return render(request, 'temperature/temperature.html')