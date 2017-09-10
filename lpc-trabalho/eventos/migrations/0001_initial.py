# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-10 03:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArtigoCientifico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('eventoPrincipal', models.CharField(max_length=128, null=True)),
                ('sigla', models.CharField(max_length=128, null=True)),
                ('dataEHoraDeInicio', models.DateTimeField(blank=True, null=True)),
                ('palavrasChave', models.CharField(max_length=128, null=True)),
                ('logoTipo', models.CharField(max_length=128, null=True)),
                ('cidade', models.CharField(max_length=128)),
                ('uf', models.CharField(max_length=128)),
                ('endereco', models.CharField(max_length=128, null=True)),
                ('cep', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eventos.Pessoa')),
                ('curriculo', models.CharField(max_length=128)),
                ('artigos', models.ManyToManyField(to='eventos.ArtigoCientifico')),
            ],
            bases=('eventos.pessoa',),
        ),
        migrations.CreateModel(
            name='EventoCientifico',
            fields=[
                ('evento_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eventos.Evento')),
                ('issn', models.CharField(max_length=128)),
            ],
            bases=('eventos.evento',),
        ),
        migrations.CreateModel(
            name='PessoaFisica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eventos.Pessoa')),
                ('cpf', models.CharField(max_length=128)),
            ],
            bases=('eventos.pessoa',),
        ),
        migrations.CreateModel(
            name='PessoaJuridica',
            fields=[
                ('pessoa_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='eventos.Pessoa')),
                ('cnpj', models.CharField(max_length=128)),
                ('razao_social', models.CharField(max_length=128)),
            ],
            bases=('eventos.pessoa',),
        ),
        migrations.AddField(
            model_name='evento',
            name='realizador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.Pessoa'),
        ),
        migrations.AddField(
            model_name='artigocientifico',
            name='autores',
            field=models.ManyToManyField(to='eventos.Autor'),
        ),
        migrations.AddField(
            model_name='artigocientifico',
            name='evento',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.EventoCientifico'),
        ),
    ]
