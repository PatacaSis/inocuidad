# Generated by Django 2.2 on 2021-04-05 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documentacion', '0014_temasnormas'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='temasnormas',
            options={'ordering': ['tema'], 'verbose_name': 'Tema de norma', 'verbose_name_plural': 'Tema de normas'},
        ),
        migrations.AddField(
            model_name='normativa',
            name='tema',
            field=models.CharField(choices=[('CIR', 'Circular'), ('CAA', 'Codigo Alimentario Argentino'), ('MEMO', 'Memorandun'), ('OS', 'Orden de Servicio'), ('R80', 'Resol 80/96 - GMC')], default=1, max_length=6, verbose_name='Tema'),
            preserve_default=False,
        ),
    ]
