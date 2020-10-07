# Generated by Django 3.1.2 on 2020-10-07 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Eventos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('horario_inicio', models.TimeField()),
                ('horario_termino', models.TimeField()),
                ('titulo', models.CharField(max_length=500)),
                ('descricao', models.TextField()),
                ('vagas', models.IntegerField()),
                ('valor', models.CharField(max_length=100)),
            ],
        ),
    ]
