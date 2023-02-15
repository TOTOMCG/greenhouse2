from django.shortcuts import render


def returnwindow(request):
    return render(request, 'window/window.html')
