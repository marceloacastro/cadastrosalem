# Generated by Django 4.0.3 on 2022-03-23 18:59

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitmembro',
            name='imagem',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to='fotos', verbose_name='Imagem'),
        ),
    ]