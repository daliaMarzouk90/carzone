from django.contrib import admin
from .models import car
from django.utils.html import format_html

class ModelCar(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<image src="{}" width="80"/>'.format(object.car_photo.url))
    
    thumbnail.short_description = 'photo'

    list_display = ("id", "car_title", "thumbnail", "price", "is_featured", "created_date")
    list_display_links = ("id", "car_title")
    list_filter = ("car_title","price", "created_date")
    search_fields = ("model",)

# Register your models here.
admin.site.register(car, ModelCar)