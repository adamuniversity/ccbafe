# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='company_about',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_address',
            field=models.TextField(max_length=400),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='v_conditions',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='v_duties',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='v_requirements',
            field=models.TextField(max_length=1000),
        ),
    ]
