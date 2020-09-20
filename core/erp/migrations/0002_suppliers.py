# Generated by Django 3.1.1 on 2020-09-10 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ruc', models.CharField(max_length=15, verbose_name='RUC')),
                ('names', models.CharField(max_length=150, verbose_name='Nombres')),
                ('direccion', models.CharField(max_length=150, verbose_name='Direccion')),
            ],
            options={
                'verbose_name': 'Proveedor',
                'verbose_name_plural': 'Proveedores',
                'ordering': ['id'],
            },
        ),
    ]
