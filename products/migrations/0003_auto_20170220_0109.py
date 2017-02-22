# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-20 06:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20160417_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='products.ProductCategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(default=products.models.get_default_category, on_delete=django.db.models.deletion.CASCADE, to='products.ProductCategory'),
        ),
    ]
