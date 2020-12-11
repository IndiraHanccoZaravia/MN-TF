# Generated by Django 3.1.2 on 2020-12-07 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metodo',
            fields=[
                ('IdMetodo', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Nombre', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Practica',
            fields=[
                ('IdPractica', models.CharField(max_length=4, primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=20)),
                ('IdMetodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculadora.metodo')),
            ],
        ),
    ]