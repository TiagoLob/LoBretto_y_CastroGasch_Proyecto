# Generated by Django 4.1.2 on 2022-11-23 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador_De_Edificios', '0005_alter_departamento_options_alter_edificio_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='noticia',
            options={'ordering': ['-fecha']},
        ),
    ]
