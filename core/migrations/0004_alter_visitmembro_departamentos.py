# Generated by Django 4.0.3 on 2022-04-14 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_visitmembro_departamentos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitmembro',
            name='departamentos',
            field=models.ManyToManyField(to='core.departamento'),
        ),
    ]
