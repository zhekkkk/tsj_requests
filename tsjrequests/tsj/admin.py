from django.contrib import admin
from .models import Worker, WorkType, WorkPosition, Apartment, Address


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'work_position')
    list_display_links = ('id', 'first_name', 'last_name')
    ordering = ['last_name']


@admin.register(WorkType)
class WorkTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'description', 'work_position')
    list_display_links = ('id', 'title')


@admin.register(WorkPosition)
class WorkPositionAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description')
    list_display_links = ('id', 'title')


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'address', 'number')
    list_display_links = ('id', 'number', 'address')
    ordering = ['id']


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'street_name', 'house_number')
    list_display_links = ('id', 'street_name', 'house_number')
    ordering = ['id']




# admin.site.register(Worker, WorkerAdmin)
