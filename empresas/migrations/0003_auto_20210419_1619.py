# Generated by Django 2.2 on 2021-04-19 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresas', '0002_auto_20210419_0901'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=100, verbose_name='Tipo producto')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre producto')),
                ('codigo', models.CharField(max_length=100, verbose_name='Codigo')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'ordering': ['tipo'],
            },
        ),
        migrations.RemoveField(
            model_name='empresa',
            name='productos',
        ),
        migrations.DeleteModel(
            name='Productos',
        ),
        migrations.AddField(
            model_name='empresa',
            name='productos_id',
            field=models.ManyToManyField(to='empresas.Producto'),
        ),
    ]
