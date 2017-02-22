# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-22 03:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170220_0109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterUniqueTogether(
            name='productcategory',
            unique_together=set([('name', 'parent')]),
        ),
    ]
