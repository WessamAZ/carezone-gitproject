from django.shortcuts import render
from requests import request

# Create your views here.
def cars(request):
    return render(request , 'cars/cars.html')