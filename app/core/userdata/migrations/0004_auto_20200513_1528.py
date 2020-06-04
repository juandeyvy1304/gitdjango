# Generated by Django 2.2.12 on 2020-05-13 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0003_auto_20200509_1310'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datosuser',
            options={'verbose_name': 'Datos de Usuario', 'verbose_name_plural': 'Información'},
        ),
        migrations.AddField(
            model_name='datosuser',
            name='adddata',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Fue creado el'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='apelUser',
            field=models.CharField(max_length=236, null=True, verbose_name='Apellido'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='geneUser',
            field=models.CharField(choices=[('Femenino', 'F'), ('Masculino', 'M'), ('Otro', 'Otro')], default='Otro', max_length=20, verbose_name='Genero'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='modifiat',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Genero modificado'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='nombUser',
            field=models.CharField(max_length=236, null=True, verbose_name='Nombres'),
        ),
        migrations.AddField(
            model_name='datosuser',
            name='profeuser',
            field=models.CharField(max_length=100, null=True, verbose_name='profesion'),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='fotoUser',
            field=models.ImageField(default='user.png', upload_to='', verbose_name='Foto de perfil'),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='teleUser',
            field=models.CharField(max_length=255, verbose_name='Teléfono'),
        ),
        migrations.AlterField(
            model_name='datosuser',
            name='userDNI',
            field=models.CharField(max_length=25, verbose_name='Identificación'),
        ),
    ]