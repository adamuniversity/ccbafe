# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20150901_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_content',
            field=models.TextField(verbose_name='Текст поста (максим 20000 симв)', default='No content'),
        ),
    ]
