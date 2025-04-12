from django.contrib import admin
from .models import Schedule, Hour

# Register your models here.
@admin.register(Schedule)
class Schedule(admin.ModelAdmin):
  list_display = ('date', 'hour', 'name', 'status')

admin.site.register(Hour)
 