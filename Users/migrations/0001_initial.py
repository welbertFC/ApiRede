# Generated by Django 3.1.2 on 2020-10-07 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=32)),
                ('criacao', models.DateTimeField(auto_now_add=True)),
                ('nome', models.CharField(max_length=150)),
                ('data_nasc', models.DateField()),
                ('igreja', models.CharField(blank=True, max_length=200, null=True)),
                ('congregacao', models.CharField(blank=True, max_length=200, null=True)),
                ('endereco', models.TextField(blank=True, null=True)),
                ('cidade', models.CharField(max_length=70)),
                ('estado', models.CharField(max_length=70)),
                ('administrador', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]