# Generated by Django 4.0.3 on 2022-03-02 17:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_alter_customusuario_primeira_visita'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customusuario',
            name='primeira_visita',
        ),
    ]