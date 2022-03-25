from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import VisitMembro


class IndexView(ListView):
    models = VisitMembro
    template_name = 'index.html'
    queryset = VisitMembro.objects.all()
    context_object_name = 'visitmembros'


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
