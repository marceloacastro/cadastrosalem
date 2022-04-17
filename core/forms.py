from django import forms
from .models import VisitMembro
from django.contrib.admin import widgets
from django.forms.widgets import NumberInput


class VisitMembroForm(forms.ModelForm):

    class Meta:
        model = VisitMembro
        fields = ['id', 'nome', 'email', 'fone', 'ativo', 'primeira_visita',
                  'data_aniversario', 'id_situacao', 'id_sexo', 'imagem', 'departamentos']

    data_aniversario = forms.DateTimeField(
        label="Data Aniversário", required=True, widget=NumberInput(attrs={'type': 'date'}))
    primeira_visita = forms.DateTimeField(
        label="Primeira Visita", required=True, widget=NumberInput(attrs={'type': 'date'}))
