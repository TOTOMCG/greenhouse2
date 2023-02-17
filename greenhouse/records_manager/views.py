#from django.shortcuts import render
from django.views.generic.list import ListView

from greenhouse.records_manager import models


#обработка модели средних значений для вывода в шаблон
class ModelName(ListView):
    model = models.AvgRecord
    template_name = 'mainlayout.html'
    context_object_name = 'avg_record'
