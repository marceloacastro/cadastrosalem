from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from stdimage.models import StdImageField


class UsuarioManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self,  email,  password,  **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff-True')

        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):

    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    SITUACAO_CHOICES = (
        ('M', 'Membro'),
        ('O', 'Obreiro'),
    )

    email = models.EmailField('E-mail', unique=True)
    fone = models.CharField('Telefone', max_length=15)
    is_staff = models.BooleanField('Membro da Equipe', default=True)
    # primeira_visita = models.DateField(
    #    'Data da Primeira Visita', auto_now_add=True)
    data_aniversario = models.DateField(
        'Data de Aniversário', default='2000-01-01')
    endereco = models.CharField('Endereço', max_length=100)
    bairro = models.CharField('Bairro', max_length=50)
    id_situacao = models.CharField(
        'Situação', max_length=1, choices=SITUACAO_CHOICES)
    id_sexo = models.CharField('Sexo', max_length=1, choices=SEXO_CHOICES)
    imagem = StdImageField('Imagem', upload_to='fotos',
                           variations={'thumb': (124, 124)})

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']

    def __str__(self):
        return self.email

    objects = UsuarioManager()
