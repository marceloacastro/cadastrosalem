# Generated by Django 4.0.3 on 2022-03-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_customusuario_data_aniversario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customusuario',
            name='id_sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Sexo'),
        ),
        migrations.AlterField(
            model_name='customusuario',
            name='id_situacao',
            field=models.CharField(choices=[('M', 'Membro'), ('O', 'Obreiro')], max_length=1, verbose_name='Situação'),
        ),
    ]