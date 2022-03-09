import imp
from django.shortcuts import render
from .models import Team
from cars.models import car

# Create your views here.

def home(request):
    team = Team.objects.all()
    featured_cars = car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = car.objects.order_by('-created_date').all()
    data = {
        "team": team
        ,"featured_cars": featured_cars
        ,"all_cars": all_cars
        }
    
    return render(request, 'pages/home.html', data)

def about(request):
    return render(request, 'pages/about.html')

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    return render(request, 'pages/contact.html')