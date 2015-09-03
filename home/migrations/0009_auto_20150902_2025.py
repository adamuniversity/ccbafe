# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20150902_2023'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='flickr_album',
            field=models.TextField(verbose_name='Код альбома для вставки', max_length=1000, default='Нет фотографий'),
        ),
    ]
