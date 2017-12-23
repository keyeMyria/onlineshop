# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-24 01:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', '男'), ('female', '女'), ('privacy', '保密')], default='privacy', max_length=12, verbose_name='性别'),
        ),
    ]
