from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def home_page(request):
    return render(request, 'index.html')

def cars_list(request):
    cars = Car.objects.all()
    return render(request, 'cars-list.html', {'cars': cars})

def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, 'car-detail.html', {'car': car})

def owner_list(request):
    owners = Owner.objects.all()
    return render(request, 'owners-list.html', {'owners': owners})
