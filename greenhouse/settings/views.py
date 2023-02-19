from django.shortcuts import render

def returnsettings(request):
    if request.method == 'POST':
        print(request.POST['value'])
    return render(request, 'settings/settings.html')