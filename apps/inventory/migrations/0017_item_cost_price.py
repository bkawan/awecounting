# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-15 10:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0016_itemcategory_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='cost_price',
            field=models.FloatField(blank=True, null=True),
        ),
    ]