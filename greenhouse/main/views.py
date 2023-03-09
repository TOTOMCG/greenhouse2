from django.shortcuts import render

# Return main .html template
def returnmain(request):
    return render(request, 'main/index.html')
