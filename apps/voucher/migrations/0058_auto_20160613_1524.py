# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-13 09:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voucher', '0057_auto_20160613_1331'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vouchersetting',
            name='show_purchase_print_location',
        ),
        migrations.RemoveField(
            model_name='vouchersetting',
            name='show_purchase_print_lot',
        ),
        migrations.RemoveField(
            model_name='vouchersetting',
            name='show_purchase_voucher_location',
        ),
        migrations.RemoveField(
            model_name='vouchersetting',
            name='show_purchase_voucher_lot',
        ),
        migrations.RemoveField(
            model_name='vouchersetting',
            name='show_sale_print_location',
        ),
        migrations.RemoveField(
            model_name='vouchersetting',
            name='show_sale_print_lot',
        ),
        migrations.RemoveField(
            model_name='vouchersetting',
            name='show_sale_voucher_location',
        ),
        migrations.RemoveField(
            model_name='vouchersetting',
            name='show_sale_voucher_lot',
        ),
    ]
