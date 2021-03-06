# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-14 11:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0060_vouchersetting_show_sale_print_sn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseorder',
            name='party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ledger.Party'),
        ),
        migrations.AlterField(
            model_name='purchasevoucher',
            name='party',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ledger.Party'),
        ),
    ]
