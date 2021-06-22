from django.contrib import admin
from cars.models import Car
from django.utils.html import format_html


class caradmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src ="{}" width="40" style="border-radius: 50px;" />'.format(object.car_photo.url))
    thumbnail.short_description = 'Photo'
    list_display = ('id', 'thumbnail', 'car_title',
                    'color', 'city', 'model', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'car_title')
    list_editable = ('is_featured',)
    search_fields = ('car_title', 'model', 'color', 'price')
    list_filter = ('color', 'model', 'car_title')


# Register your models here.
admin.site.register(Car, caradmin)
