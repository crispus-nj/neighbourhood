from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Location, Business

class LocationStyle(UserAdmin):
    list_display = ('name', 'county')
    filter_horizontal = ()
    fieldsets = ()
    ordering = ()
    list_filter = ()


admin.site.register(Location, LocationStyle)
admin.site.register(Business)