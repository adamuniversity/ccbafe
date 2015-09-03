# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20150830_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_flickr_albumId',
            field=models.CharField(max_length=300, default='Нет фотографий', verbose_name='Flickr Album ID'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='v_added',
            field=models.DateTimeField(verbose_name='Дата публикации'),
        ),
    ]
