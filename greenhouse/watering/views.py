from django.shortcuts import render

def returnwatering(request):
    return render(request, 'watering/watering.html')

