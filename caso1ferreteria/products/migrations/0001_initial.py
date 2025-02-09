# Generated by Django 3.2 on 2021-05-30 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FamiliaProducto',
            fields=[
                ('id_familia', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_familia', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'familia_producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_producto', models.CharField(max_length=30)),
                ('fecha_vencimiento', models.DateField(blank=True, null=True)),
                ('descripcion', models.CharField(max_length=100)),
                ('precio_clp', models.IntegerField()),
                ('precio_usd', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('foto', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'producto',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('id_proveedor', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre_proveedor', models.CharField(max_length=50)),
                ('rut_proveedor', models.CharField(max_length=10)),
                ('celular', models.BigIntegerField()),
                ('correo', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'proveedor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id_tipo', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_tipo', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'tipo_producto',
                'managed': False,
            },
        ),
    ]
