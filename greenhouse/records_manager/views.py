from django.shortcuts import render


def records_page(request):
    return render(request, 'records.html')
