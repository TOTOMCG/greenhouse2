from django.shortcuts import render


def returdatabase(request):
    return render(request, 'database/database.html')