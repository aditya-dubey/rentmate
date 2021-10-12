# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-07 09:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ment_form', '0003_auto_20161020_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='apartment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locality', models.CharField(max_length=15)),
                ('address', models.TextField()),
                ('idproof', models.FileField(upload_to='')),
                ('houseimage', models.FileField(upload_to='')),
                ('space', models.IntegerField(max_length=1)),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('price', models.IntegerField()),
                ('info', models.IntegerField(blank=True, default=0, null=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
