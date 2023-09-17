from django import forms
from django.contrib import admin
from .models import Perfil, Evento, Actividad, Asistencia

class AsistenciaAdminForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'instance' in kwargs:
            if self.instance.id:
                if self.instance.docente:
                    self.fields['docente'].queryset = Perfil.objects.filter(tipo='docente')
                else:
                    self.fields['estudiante'].queryset = Perfil.objects.filter(tipo='estudiante')

