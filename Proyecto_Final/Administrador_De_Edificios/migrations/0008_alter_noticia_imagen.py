# Generated by Django 4.1.2 on 2022-11-24 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador_De_Edificios', '0007_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='imagen',
            field=models.ImageField(upload_to='noticias'),
        ),
    ]
