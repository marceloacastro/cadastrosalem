from inspect import _empty
from queue import Empty
from typing import KeysView
from django.contrib.auth.models import User
from asyncore import write
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from itertools import chain
from django.shortcuts import get_object_or_404, render
from .models import VisitMembro
from django.contrib.auth.models import User
from datetime import timedelta
from django.utils import timezone
from django.http import HttpResponse
from selenium import webdriver
import os
from time import sleep
from .forms import VisitMembroForm


class IndexView(TemplateView):
    models = VisitMembro
    template_name = 'index.html'
    queryset = VisitMembro.objects.all()
    context_object_name = 'visitmembro'
    paginate_by = 10
    ordering = 'nome'


class MenuInicialView(ListView):
    models = VisitMembro
    template_name = 'menu_inicial.html'
    queryset = VisitMembro.objects.all()
    context_object_name = 'visitmembro'
    paginate_by = 10
    ordering = 'nome'


def home_whatsapp(request):
    return render(request, "home_whatsapp.html")


class zapbot:
    # O caminho do chromedriver
    dir_path = 'C:/Marcelo/ProjetosPython/CadastroSalem/staticfiles/admin/chromedriver/'
    chromedriver = os.path.join(dir_path, "chromedriver.exe")
    # Caminho onde será criada pasta profile
    profile = os.path.join(dir_path, "profile", "wpp")

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        # Configurando a pasta profile, para mantermos os dados da seção
        self.options.add_argument(
            r"user-data-dir={}".format(self.profile))
        # Inicializa o webdriver
        self.driver = webdriver.Chrome(
            self.chromedriver, chrome_options=self.options)
        # Abre o whatsappweb
        self.driver.get("https://web.whatsapp.com/")
        # Aguarda alguns segundos para validação manual do QrCode
        self.driver.implicitly_wait(15)

    def ultima_msg(self):
        """ Captura a ultima mensagem da conversa """
        try:
            post = self.driver.find_elements_by_class_name("_3_7SH")
            ultimo = len(post) - 1
            # O texto da ultima mensagem
            texto = post[ultimo].find_element_by_css_selector(
                "span.selectable-text").text
            return texto
        except Exception as e:
            print("Erro ao ler msg, tentando novamente!")

    def envia_media(self, fileToSend):
        """ Envia media """
        try:
            # Clica no botão adicionar
            self.driver.find_element_by_css_selector(
                "span[data-icon='clip']").click()
            # Seleciona input
            attach = self.driver.find_element_by_css_selector(
                "input[type='file']")
            # Adiciona arquivo
            attach.send_keys(fileToSend)
            sleep(3)
            # Seleciona botão enviar
            send = self.driver.find_element_by_xpath(
                "//div[contains(@class, 'yavlE')]")
            # Clica no botão enviar
            send.click()
        except Exception as e:
            print("Erro ao enviar media", e)

    def abre_conversa(self, contato):
        """ Abre a conversa com um contato especifico """
        try:
            # Seleciona a caixa de pesquisa de conversa
            self.caixa_de_pesquisa = self.driver.find_element_by_xpath(
                '//*[@id = "side"]/div[1]/div/label/div/div[2]')
            # Digita o nome ou numero do contato
            self.caixa_de_pesquisa.send_keys(contato)
            sleep(2)
            # Seleciona o contato
            self.contato = self.driver.find_element_by_xpath(
                "//span[@title = '{}']".format(contato))
            # Entra na conversa
            self.contato.click()
        except Exception as e:
            raise e

    def envia_msg(self, msg):
        """ Envia uma mensagem para a conversa aberta """
        try:
            sleep(2)
            # Seleciona acaixa de mensagem
            self.caixa_de_mensagem = self.driver.find_element_by_xpath(
                '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
            # Digita a mensagem
            self.caixa_de_mensagem.send_keys(msg)
            sleep(1)
            # Seleciona botão enviar
            self.botao_enviar = self.driver.find_element_by_class_name(
                "_4sWnG")
            # Envia msg
            self.botao_enviar.click()
            sleep(2)
        except Exception as e:
            print("Erro ao enviar msg", e)


def send_whatsapp(request):
    if request.method == 'POST':
        Ph = request.POST['Phone']
        Message = request.POST['Message']
        bot = zapbot()
        bot.abre_conversa(Ph)
        bot.envia_msg(Message)
        MsgRetorno = "Mensagem Enviada com Sucesso."
        return render(request, "home_whatsapp.html", {'msg': MsgRetorno})
    else:
        return HttpResponse("<h1>404 - Not Found>")


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
    form_class = VisitMembroForm
    template_name = 'visitmembro_form.html'
    success_url = reverse_lazy('menu_inicial')


class UpdateVisitMembroView(UpdateView):
    model = VisitMembro
    form_class = VisitMembroForm
    template_name = 'visitmembro_form.html'
    success_url = reverse_lazy('menu_inicial')


class DeleteVisitMembroView(DeleteView):
    model = VisitMembro
    template_name = 'visitmembro_del.html'
    success_url = reverse_lazy('menu_inicial')
