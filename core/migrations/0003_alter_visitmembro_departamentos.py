# Generated by Django 4.0.3 on 2022-04-03 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_visitmembro_data_aniversario_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitmembro',
            name='departamentos',
            field=models.ManyToManyField(default=1, to='core.departamento'),
        ),
    ]
