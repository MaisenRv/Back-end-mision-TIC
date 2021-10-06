# Generated by Django 3.2.7 on 2021-10-06 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HVApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HojaDeVida',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20, unique=True)),
                ('apellido', models.CharField(max_length=20)),
                ('cedula', models.CharField(max_length=12)),
                ('correo', models.EmailField(max_length=100)),
                ('Agnos_experiencia', models.CharField(max_length=3)),
                ('profecion', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
            ],
        ),
    ]
