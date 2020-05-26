from django.contrib import admin
from core.models import Event

# Register your models here.

class EventAdmin(admin.ModelAdmin):
  list_display = ('title', 'event_date', 'datetimestamp') 
  list_filter = ('user', 'title', 'event_date',)

admin.site.register(Event, EventAdmin)