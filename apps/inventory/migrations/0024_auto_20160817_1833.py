# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 12:48
from __future__ import unicode_literals

from django.db import migrations
import njango.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0023_auto_20160815_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalentry',
            name='date',
            field=njango.fields.BSDateField(),
        ),
    ]
