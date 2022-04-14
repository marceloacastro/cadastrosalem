from django.contrib.auth.models import User
from .models import VisitMembro
import django_filters


class UserFilter(django_filters.FilterSet):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', ]


class VisitanteFilter(django_filters.FilterSet):
    class Meta:
        model = VisitMembro
        fields = ['nome', 'data_aniversario', 'primeira_visita', ]
