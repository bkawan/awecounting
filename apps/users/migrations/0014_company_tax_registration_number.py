# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-05 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_auto_20160304_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='tax_registration_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]