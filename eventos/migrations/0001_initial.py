# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-31 00:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('descricao', models.TextField()),
                ('sigla', models.CharField(max_length=10)),
                ('ano', models.IntegerField()),
                ('logo', models.ImageField(upload_to='')),
                ('data_inicio', models.DateTimeField()),
                ('data_fim', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
            },
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField()),
                ('festa_evento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventos', to='eventos.Evento')),
            ],
            options={
                'verbose_name': 'Inscrição',
                'verbose_name_plural': 'Inscrições',
            },
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('idade', models.CharField(max_length=3)),
                ('cpf', models.CharField(max_length=11)),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pessoa',
                'verbose_name_plural': 'Pessoas',
            },
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=128)),
                ('descricao', models.CharField(max_length=128)),
                ('preco', models.FloatField()),
                ('evento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.Evento')),
            ],
            options={
                'verbose_name': 'Ticket',
                'verbose_name_plural': 'Tickets',
            },
        ),
        migrations.AddField(
            model_name='inscricao',
            name='participante',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='participantes', to='eventos.Pessoa'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='ticket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eventos.Ticket'),
        ),
        migrations.AddField(
            model_name='evento',
            name='realizador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='realizadores', to='eventos.Pessoa'),
        ),
    ]
