# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20150830_1322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='news_short_content',
        ),
    ]
