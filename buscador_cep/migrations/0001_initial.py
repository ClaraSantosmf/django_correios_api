# Generated by Django 4.0.6 on 2022-07-13 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ConsultarCep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cep', models.CharField(max_length=8, unique=True)),
                ('cidade', models.CharField(max_length=48)),
                ('bairro', models.CharField(max_length=48)),
                ('rua', models.CharField(max_length=64)),
                ('complemento', models.CharField(blank=True, max_length=64)),
            ],
        ),
    ]
