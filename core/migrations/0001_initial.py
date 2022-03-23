# Generated by Django 4.0.3 on 2022-03-23 18:45

from django.db import migrations, models
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VisitMembro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('fone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('primeira_visita', models.DateField(default='2000-01-01', verbose_name='Data da Primeira Visita')),
                ('data_aniversario', models.DateField(default='2000-01-01', verbose_name='Data de Aniversário')),
                ('id_situacao', models.CharField(choices=[('V', 'Visitante'), ('M', 'Membro'), ('O', 'Obreiro')], max_length=1, verbose_name='Situação')),
                ('id_sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Sexo')),
                ('imagem', stdimage.models.StdImageField(null=True, upload_to='fotos', verbose_name='Imagem')),
            ],
        ),
    ]