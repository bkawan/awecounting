# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 12:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0009_auto_20160610_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationcontain',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_contain', to='inventory.Item'),
        ),
    ]
