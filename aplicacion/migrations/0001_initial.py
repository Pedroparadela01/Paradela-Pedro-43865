# Generated by Django 4.2.3 on 2023-08-10 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Buzos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('talle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cargos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('talle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Remeras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('talle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reparto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=50)),
                ('fecha_entrega', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vermudas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=50)),
                ('talle', models.CharField(max_length=50)),
            ],
        ),
    ]