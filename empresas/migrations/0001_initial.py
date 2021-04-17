# Generated by Django 2.2 on 2021-04-05 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Razon Social')),
                ('numero', models.CharField(max_length=20, unique=True, verbose_name='Identificacion')),
                ('localidad', models.CharField(max_length=50, verbose_name='Localidad')),
                ('domicilio', models.CharField(max_length=50, verbose_name='Ubicacion')),
                ('productos', models.CharField(max_length=50, verbose_name='Productos')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ['nombre'],
            },
        ),
    ]