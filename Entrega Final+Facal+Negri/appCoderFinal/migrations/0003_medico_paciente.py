# Generated by Django 3.2.9 on 2021-12-13 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appCoderFinal', '0002_jugador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=40)),
                ('especialidad', models.CharField(max_length=40)),
                ('activo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellido', models.CharField(max_length=40)),
                ('obrasocial', models.CharField(max_length=40)),
                ('edad', models.IntegerField()),
            ],
        ),
    ]