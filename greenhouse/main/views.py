from django.shortcuts import render

def returnmain(request):
    return render(request, 'main/main.html')
