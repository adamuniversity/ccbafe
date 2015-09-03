# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_news_news_short_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcements',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('announce_title', models.CharField(max_length=255, verbose_name='Заголовок поста')),
                ('slug', models.SlugField(max_length=255, verbose_name='Идентификатор')),
                ('announce_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('announce_image', models.ImageField(verbose_name='Изображение статьи', upload_to='images/post_images')),
                ('announce_content', models.TextField(max_length=10000, verbose_name='Текст поста (максим 10000 симв)', default='No content')),
                ('announce_author', models.ForeignKey(to='home.UserFullName', verbose_name='Автор статьи', default='1')),
            ],
            options={
                'ordering': ['-announce_date'],
                'verbose_name': 'Анонс',
                'verbose_name_plural': 'Анонсы',
            },
        ),
        migrations.RenameField(
            model_name='news',
            old_name='news_slug',
            new_name='slug',
        ),
        migrations.AddField(
            model_name='company',
            name='company_type',
            field=models.CharField(max_length=100, verbose_name='Форма собственности', default=datetime.datetime(2015, 8, 30, 8, 28, 13, 120686, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='company',
            name='company_about',
            field=models.TextField(max_length=1000, verbose_name='Информация об организации'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_address',
            field=models.TextField(max_length=400, verbose_name='Адрес организации'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_contactPerson',
            field=models.CharField(max_length=100, verbose_name='Контактное лицо компании'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_email',
            field=models.CharField(max_length=50, verbose_name='Электронная почта'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=150, verbose_name='Нименование организации'),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_phone',
            field=models.CharField(max_length=100, verbose_name='Контактные телефоны'),
        ),
    ]
