# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20150901_2006'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announce', models.ForeignKey(verbose_name='Анонсы', to='home.Announcements')),
            ],
        ),
        migrations.RemoveField(
            model_name='news',
            name='news_flickr_albumId',
        ),
        migrations.AddField(
            model_name='news',
            name='flickr_album',
            field=models.TextField(max_length=300, verbose_name='Код альбома для вставки', default='Нет фотографий'),
        ),
        migrations.AddField(
            model_name='main',
            name='news',
            field=models.ForeignKey(verbose_name='Новости', to='home.News'),
        ),
        migrations.AddField(
            model_name='main',
            name='vacancy',
            field=models.ForeignKey(verbose_name='Вакансии', to='home.Vacancy'),
        ),
    ]
