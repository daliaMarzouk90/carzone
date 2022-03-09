from django.shortcuts import render, get_list_or_404
from .models import car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def cars(request):
    all_cars = car.objects.order_by('-created_date')
    paginator = Paginator(all_cars, 2)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    data = {
        "all_cars": paged_cars
        }
    return render(request, 'cars/cars.html', data)

def car_details(request, car_id):
    single_car = get_list_or_404(car, id=car_id)
    data = {"car": single_car[0],}
    return render(request, "cars/car-details.html", data)

def search(request):
    featured_cars = car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = car.objects.order_by('-created_date').all()
    data = { 
        "featured_cars": featured_cars
        }
    return render(request, "cars/search.html", data)