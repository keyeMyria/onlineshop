# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-22 19:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=100, verbose_name='商品名'),
        ),
    ]
