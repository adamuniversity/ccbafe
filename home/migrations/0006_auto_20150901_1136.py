# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20150830_1428'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='announcements',
            options={'verbose_name': 'Анонс', 'verbose_name_plural': 'Анонсы', 'ordering': ['-date']},
        ),
        migrations.RenameField(
            model_name='announcements',
            old_name='announce_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='announcements',
            old_name='announce_content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='announcements',
            old_name='announce_date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='announcements',
            old_name='announce_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='announcements',
            old_name='announce_title',
            new_name='title',
        ),
        migrations.AlterField(
            model_name='news',
            name='news_author',
            field=models.ForeignKey(verbose_name='Автор статьи', to=settings.AUTH_USER_MODEL, default='1'),
        ),
    ]
