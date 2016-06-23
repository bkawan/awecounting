# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-23 07:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def delete_all_locations(apps, schema_editor):
    from apps.inventory.models import Location
    from django.db import connection

    cursor = connection.cursor()
    cursor.execute("TRUNCATE TABLE " + Location._meta.db_table + " CASCADE;")


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0010_subscription_enable_lot'),
        ('inventory', '0017_item_cost_price'),
    ]

    operations = [
        migrations.RunPython(delete_all_locations),
        migrations.AddField(
            model_name='location',
            name='company',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='inventory_locations',
                                    to='users.Company'),
            preserve_default=False,
        ),
    ]