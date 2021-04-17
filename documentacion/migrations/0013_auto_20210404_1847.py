# Generated by Django 2.2 on 2021-04-04 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0012_auto_20210404_1123'),
    ]

    operations = [
        migrations.CreateModel(
            name='Normativa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(verbose_name='Fecha del documento')),
                ('tipo', models.CharField(choices=[('CIR', 'Circular'), ('CAA', 'Codigo Alimentario Argentino'), ('MEMO', 'Memorandun'), ('OS', 'Orden de Servicio'), ('R80', 'Resol 80/96 - GMC')], max_length=4, verbose_name='Tipo de norma')),
                ('numero', models.CharField(blank=True, max_length=10, null=True, verbose_name='Numero del documento')),
                ('titulo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Titulo de documento')),
                ('texto', models.FileField(blank=True, null=True, upload_to='normativas')),
                ('pais', models.CharField(blank=True, max_length=100, null=True, verbose_name='Pais a exportar')),
            ],
            options={
                'verbose_name': 'Normativa',
                'verbose_name_plural': 'Normativas',
                'ordering': ['tipo', 'fecha'],
            },
        ),
        migrations.DeleteModel(
            name='Norma',
        ),
        migrations.DeleteModel(
            name='NormaOperativa',
        ),
        migrations.DeleteModel(
            name='RequisitosExpo',
        ),
    ]
