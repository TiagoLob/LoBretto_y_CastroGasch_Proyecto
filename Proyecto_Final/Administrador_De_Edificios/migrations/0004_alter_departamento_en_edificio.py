# Generated by Django 4.1.2 on 2022-11-22 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Administrador_De_Edificios', '0003_alter_inquilino_vive_en_departamento_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departamento',
            name='en_Edificio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrador_De_Edificios.edificio'),
        ),
    ]
