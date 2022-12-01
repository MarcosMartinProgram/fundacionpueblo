from django.contrib import admin
from .models import Eventos

# Register your models here.

class EventosAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

admin.site.register(Eventos, EventosAdmin) 