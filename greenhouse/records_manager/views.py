#from django.shortcuts import render
from django.views.generic.list import ListView

#обработка модели средних значений для вывода в шаблон
class ModelName(ListView):
    model = ModelName
    template_name = 'main.html'
    context_object_name = 'average'
