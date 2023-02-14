from django.shortcuts import render

def returnsettings(request):
    return render(request, 'settings/settings.html')