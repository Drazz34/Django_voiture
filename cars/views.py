from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Car
from .forms import CarForm


def detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    context = {'car': car}
    return render(request, 'cars/detail.html', context)


def note(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('detail', car_id=car.id)
    else:
        form = CarForm(instance=car)

    context = {'form': form, 'car': car}
    return render(request, 'cars/note.html', context)

def index(request):
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, 'cars/index.html', context)

