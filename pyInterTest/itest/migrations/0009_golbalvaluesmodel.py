# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-11 11:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itest', '0008_auto_20170911_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='golbalValuesModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('value', models.TextField()),
                ('type', models.TextField(default='string')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itest.Project')),
            ],
        ),
    ]