# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-12-20 01:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30, verbose_name='\u516c\u53f8\u540d\u79f0')),
            ],
            options={
                'verbose_name': '\u54c1\u724c',
                'verbose_name_plural': '\u54c1\u724c',
            },
        ),
    ]
