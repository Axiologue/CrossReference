# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ethicstag',
            name='article',
            field=models.ForeignKey(to='refData.Article', related_name='ethicstags'),
        ),
        migrations.AlterField(
            model_name='metatag',
            name='article',
            field=models.ForeignKey(to='refData.Article', related_name='metatags'),
        ),
    ]