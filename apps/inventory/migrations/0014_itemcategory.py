# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-14 09:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0013_auto_20160612_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=254, null=True)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='inventory.ItemCategory')),
            ],
            options={
                'verbose_name_plural': 'Item Categories',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
