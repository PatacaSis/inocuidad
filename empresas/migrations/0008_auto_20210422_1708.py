# Generated by Django 2.2 on 2021-04-22 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0007_auto_20210422_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empresa',
            name='lineas_haccp',
            field=models.CharField(max_length=300, verbose_name='Lineas de produccion con HACCP:'),
        ),
    ]
