# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-05-23 05:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0003_auto_20200523_1101'),
    ]

    operations = [
        migrations.AddField(
            model_name='lab',
            name='img',
            field=models.IntegerField(default=1),
        ),
    ]
