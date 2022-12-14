# Generated by Django 4.1.2 on 2022-11-23 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Administrador_De_Edificios', '0004_alter_departamento_en_edificio'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='departamento',
            options={'ordering': ['en_Edificio', 'piso_Y_Letra']},
        ),
        migrations.AlterModelOptions(
            name='edificio',
            options={'ordering': ['nombre']},
        ),
        migrations.AlterModelOptions(
            name='inquilino',
            options={'ordering': ['vive_En_Edificio', 'apellido', 'nombre']},
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=254)),
                ('subtitulo', models.CharField(max_length=254)),
                ('cuerpo', models.TextField()),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='noticias')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
