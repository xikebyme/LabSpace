# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2020-05-20 08:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_auto_20200520_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='题目')),
                ('link', models.CharField(max_length=5000, verbose_name='链接')),
                ('add_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建日期')),
                ('mod_date', models.DateTimeField(auto_now=True, verbose_name='最后修改日期')),
                ('like_num', models.IntegerField(default=0, verbose_name='推荐数')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
        ),
    ]
