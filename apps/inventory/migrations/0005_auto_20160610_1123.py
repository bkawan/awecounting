# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_item_oem_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='oem_no',
            field=models.CharField(blank=True, max_length=250, null=True, verbose_name=b'OEM No.'),
        ),
    ]