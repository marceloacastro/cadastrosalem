import uuid
from django.db import models
from stdimage.models import StdImageField


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Departamento(models.Model):
    departamento = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.departamento


class VisitMembro(models.Model):

    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    SITUACAO_CHOICES = (
        ('V', 'Visitante'),
        ('M', 'Membro'),
        ('O', 'Obreiro'),
    )

    id = models.BigAutoField(primary_key=True, auto_created=True)
    nome = models.CharField('Nome', max_length=50, null=False)
    email = models.EmailField('E-mail', null=False)
    fone = models.CharField('Telefone', max_length=15, null=False)
    ativo = models.BooleanField('Ativo?', default=True)
    primeira_visita = models.DateField(
        'Data da Primeira Visita', default='01/01/2000',  null=False)
    data_aniversario = models.DateField(
        'Data de Aniversário', default='01/01/2000',  null=False)
    id_situacao = models.CharField(
        'Situação', max_length=1, choices=SITUACAO_CHOICES,  null=False)
    id_sexo = models.CharField(
        'Sexo', max_length=1, choices=SEXO_CHOICES,   null=False)
    imagem = StdImageField('Imagem', upload_to=get_file_path,
                           variations={'thumb': (124, 124)}, delete_orphans=True, blank=True)
    departamentos = models.ManyToManyField(Departamento)

    def __str__(self):
        return self.nome

    REQUIRED_FIELDS = ['id', 'nome', 'email']
