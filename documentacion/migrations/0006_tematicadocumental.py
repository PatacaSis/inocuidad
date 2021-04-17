# Generated by Django 2.2 on 2021-04-01 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0005_normaoperativa_tema'),
    ]

    operations = [
        migrations.CreateModel(
            name='TematicaDocumental',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50, unique=True)),
                ('texto', models.CharField(max_length=150)),
                ('imagen', models.ImageField(upload_to='principal')),
            ],
            options={
                'verbose_name': 'Clasificacion de norma',
                'verbose_name_plural': 'Clasificacion de normas',
                'ordering': ['titulo'],
            },
        ),
    ]