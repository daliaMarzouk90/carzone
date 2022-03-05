from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('cars', views.cars, name='cars'),
]
