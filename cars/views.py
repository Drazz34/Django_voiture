from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Car


def detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    context = {'car': car}
    return render(request, 'cars/detail.html', context)


def index(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'cars/index.html', context)
