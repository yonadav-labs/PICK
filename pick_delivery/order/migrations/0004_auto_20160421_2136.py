# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-21 21:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
