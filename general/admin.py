from django.contrib import admin
from .models import *
from . import form
# Register your models here.

class AsistenciaAdmin(admin.ModelAdmin):
    form = form.AsistenciaAdminForm




admin.site.register(Perfil)
admin.site.register(Evento)
admin.site.register(Actividad)
admin.site.register(Asistencia, AsistenciaAdmin)
