from django.shortcuts import render
from django.http import HttpResponse
from .models import Car

def index(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'cars/index.html', context)
