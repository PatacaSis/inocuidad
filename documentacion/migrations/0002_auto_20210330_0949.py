# Generated by Django 2.2 on 2021-03-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='norma',
            name='identificacion',
            field=models.CharField(max_length=200, verbose_name='Identificacion de la norma'),
        ),
    ]
