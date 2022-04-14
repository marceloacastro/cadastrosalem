from django.contrib import admin
from .models import Departamento, VisitMembro


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('departamento',)


@admin.register(VisitMembro)
class VisitMembroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')
