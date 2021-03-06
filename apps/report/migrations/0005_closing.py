# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-10 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_subscription_enable_lot'),
        ('report', '0004_balancesheetreportsetting'),
    ]

    operations = [
        migrations.CreateModel(
            name='Closing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fy', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('inventory_balance', models.FloatField()),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Company')),
            ],
        ),
    ]
