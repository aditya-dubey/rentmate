# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ment_form', '0005_auto_20161107_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartment',
            name='info',
            field=models.IntegerField(),
        ),
    ]