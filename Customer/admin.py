from django.contrib import admin
from .models import Customer

# Register your models here.
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'password')
    search_fields = ['name']
