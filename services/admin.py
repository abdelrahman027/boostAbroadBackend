from django.contrib import admin

from .models import Service,Location,knowledgehub,Event
# Register your models here.

admin.site.register(Service)
admin.site.register(Location)
admin.site.register(knowledgehub)
admin.site.register(Event)

