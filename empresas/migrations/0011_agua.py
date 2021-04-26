# Generated by Django 2.2 on 2021-04-26 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0010_auditoria_grupos_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agua',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('tipo_agua', models.CharField(choices=[('Os', 'Agua de osmosis'), ('Po', 'Agua de pozo'), ('Re', 'Agua de red')], max_length=2, verbose_name='Fuente de agua ')),
                ('punto_muestreo', models.CharField(max_length=50, verbose_name='Punto de muestreo')),
                ('tipo_analisis', models.CharField(choices=[('MB', 'Microbiologico'), ('FQ', 'Fisicoquimico')], max_length=2, verbose_name='Tipo de analisis')),
                ('laboratorio', models.CharField(max_length=50, verbose_name='Laboratorio')),
                ('resultado', models.BooleanField(verbose_name='Aceptable/No aceptable')),
                ('observaciones', models.TextField(verbose_name='Observaciones')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresas.Empresa')),
            ],
            options={
                'verbose_name': 'Muestreo de agua',
                'verbose_name_plural': 'Muestreos de agua',
                'ordering': ['fecha'],
            },
        ),
    ]
