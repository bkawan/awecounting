# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-28 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0007_auto_20160523_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='related_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_party', to='users.Company'),
        ),
    ]
