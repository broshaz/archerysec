# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-01 06:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('osintscan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osint_domain_db',
            name='domains',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='osint_domain_db',
            name='project_id',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='osint_domain_db',
            name='sub_domains',
            field=models.TextField(blank=True, null=True),
        ),
    ]
