from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('cars', views.cars, name='cars'),
    path('car_details/<int:car_id>', views.car_details, name='car_details'),
    path('search', views.search, name='search'),
]
