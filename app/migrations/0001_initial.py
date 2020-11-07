# Generated by Django 3.1.1 on 2020-11-06 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('nro_doc', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('tipo_doc', models.CharField(max_length=20)),
                ('nombre_completo', models.CharField(max_length=50)),
                ('fecha_nac', models.DateField(max_length=20)),
                ('genero', models.CharField(max_length=20)),
                ('telefono', models.IntegerField(default=0)),
                ('email', models.EmailField(max_length=50)),
                ('pasword', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=250)),
                ('ofertas', models.BooleanField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=250)),
                ('url', models.CharField(max_length=100)),
                ('href', models.CharField(max_length=100)),
                ('precio', models.FloatField(max_length=20)),
                ('cod_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fec_prestamo', models.DateField(max_length=20)),
                ('fec_devolucion', models.DateField(max_length=20)),
                ('cod_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.cliente')),
                ('cod_prod', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
            ],
        ),
    ]
