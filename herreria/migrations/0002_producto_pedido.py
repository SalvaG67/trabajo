# Generated by Django 5.1.7 on 2025-03-11 22:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('herreria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.FloatField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herreria.cliente')),
                ('vendedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='herreria.vendedor')),
                ('productos', models.ManyToManyField(to='herreria.producto')),
            ],
        ),
    ]
