# Generated by Django 2.2.12 on 2020-05-09 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='datosuser',
            options={'verbose_name': 'datos de usuario', 'verbose_name_plural': 'informacion'},
        ),
        migrations.AlterModelOptions(
            name='habilidades',
            options={'verbose_name': 'habilidades del usuario', 'verbose_name_plural': 'competencias'},
        ),
        migrations.AlterModelOptions(
            name='roles',
            options={'verbose_name': 'perfiles de usuario', 'verbose_name_plural': 'perfiles'},
        ),
    ]
