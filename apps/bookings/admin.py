from django.contrib import admin
from .models import Booking

# Register your models here.
@admin.register(Booking)
class Schedule(admin.ModelAdmin):
  list_display = ('date', 'hour', 'name', 'status')