from inspect import _empty
from queue import Empty
from django.contrib.auth.models import User
from asyncore import write
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from psycopg2 import Date
from itertools import chain
from django.shortcuts import get_object_or_404, render
from .models import VisitMembro
from django.contrib.auth.models import User
from .filters import UserFilter, VisitanteFilter
from search_listview.list import SearchableListView
from datetime import timedelta
from django.utils import timezone


def search(request):
    user_list = User.objects.all()
    user_filter = UserFilter(request.GET, queryset=user_list)
    return render(request, 'search/user_list.html', {'filter': user_filter})


def search_visitante(request):
    visitante_list = VisitMembro.objects.all()
    visitante_filter = VisitanteFilter(request.GET, queryset=visitante_list)
    return render(request, 'search/user_list.html', {'filter': visitante_filter})


class IndexView(ListView):
    model = VisitMembro
    template_name = 'index.html'
    paginate_by = 10
    ordering = 'nome'
    searchable_fields = ["nome", "primeira_visita", "data_aniversario"]
    specifications = {
        "primeira_visita": "__icontains"
    }


class ListVisitView(ListView):
    models = VisitMembro
    template_name = 'list_visitday.html'
    queryset = VisitMembro.objects.order_by('nome').all()
    queryset = VisitMembro.objects.all()
    context_object_name = 'visitmembros'


class ListsView(ListView):
    models = VisitMembro
    template_name = 'list.html'
    context_object_name = 'visitmembros'

    def get_queryset(self, *args, **kwargs):

        queryset = VisitMembro.objects.order_by(
            'data_aniversario__month',
            'data_aniversario__day',
            'nome').all()

        if self.request.GET.get("filter") == 'primeira_visita':
            v_visita = self.request.GET.get("q")
            queryset = queryset.filter(primeira_visita=v_visita).all()

        elif self.request.GET.get("filter") == 'nome':
            queryset = queryset.filter(
                nome__contains=self.request.GET.get("q")).all()

        elif self.request.GET.get("filter") == 'data_aniversario':
            datetime_now = timezone.now()
            now_day, now_month = datetime_now.day, datetime_now.month
            datetime_sevendays = datetime_now + \
                timedelta(days=int(self.request.GET.get("q")))
            sevendays_day, sevendays_month = datetime_sevendays.day, datetime_sevendays.month
            queryset = VisitMembro.objects.all()
            if now_month == sevendays_month:
                queryset = queryset.filter(
                    data_aniversario__month=now_month,
                    data_aniversario__day__gte=now_day,
                    data_aniversario__day__lte=sevendays_day,
                )
            else:
                queryset = queryset.filter(
                    Q(data_aniversario__month=now_month,
                      data_aniversario__day__gte=now_day) |
                    Q(data_aniversario__month=sevendays_month,
                      data_aniversario__day__lte=sevendays_day)
                )
        return queryset


class CreateVisitMembroView(CreateView):
    model = VisitMembro
    template_name = 'visitmembro_form.html'
    fields = ['id', 'nome', 'email', 'fone', 'ativo', 'primeira_visita',
              'data_aniversario', 'id_situacao', 'id_sexo', 'imagem', 'departamentos']
    success_url = reverse_lazy('index')


class UpdateVisitMembroView(UpdateView):
    model = VisitMembro
    template_name = 'visitmembro_form.html'
    fields = ['id', 'nome', 'email', 'fone', 'ativo', 'primeira_visita',
              'data_aniversario', 'id_situacao', 'id_sexo', 'imagem', 'departamentos']
    success_url = reverse_lazy('index')


class DeleteVisitMembroView(DeleteView):
    model = VisitMembro
    template_name = 'visitmembro_del.html'
    success_url = reverse_lazy('index')
