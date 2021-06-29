from django.contrib import admin
from contacts.models import Contact


class contactadmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email',
                    'car_title', 'city', 'create_date')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'car_title')
    list_per_page = 25


# Register your models here.

admin.site.register(Contact, contactadmin)
