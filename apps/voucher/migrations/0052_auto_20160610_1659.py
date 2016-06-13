# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-10 11:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0051_auto_20160610_1639'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lot',
            name='lot_item_details',
        ),
        migrations.AddField(
            model_name='lotitemdetail',
            name='lot',
            field=models.ForeignKey(default=4, on_delete=django.db.models.deletion.CASCADE, related_name='lot_item_details', to='voucher.Lot'),
            preserve_default=False,
        ),
    ]
