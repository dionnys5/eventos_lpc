# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-23 23:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='endereco',
        ),
        migrations.RemoveField(
            model_name='pessoa',
            name='endereco',
        ),
        migrations.DeleteModel(
            name='Endereco',
        ),
    ]
