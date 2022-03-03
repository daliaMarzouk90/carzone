from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.
class ModelAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<image src="{}" width="40" style="border-radius: 50px;"/>'.format(object.photo.url))
    
    thumbnail.short_description = 'photo'

    list_display = ("id", "thumbnail", "first_name", "last_name", "designation", "created_date")
    list_display_links = ("id", "first_name")
    list_filter = ("first_name","designation", "created_date")
    search_fields = ("first_name", "last_name", "designation")

admin.site.register(Team, ModelAdmin)