# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company_name', models.CharField(max_length=150)),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='Идентификатор')),
                ('company_address', models.CharField(max_length=400)),
                ('company_phone', models.CharField(max_length=100)),
                ('company_contactPerson', models.CharField(max_length=100)),
                ('company_email', models.CharField(max_length=50)),
                ('company_about', models.CharField(max_length=1000)),
            ],
            options={
                'verbose_name': 'Компания',
                'verbose_name_plural': 'Компании',
                'ordering': ['-company_name'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news_title', models.CharField(verbose_name='Заголовок поста', max_length=255)),
                ('news_slug', models.SlugField(max_length=255, verbose_name='Идентификатор')),
                ('news_date', models.DateTimeField(verbose_name='Дата публикации')),
                ('news_image', models.ImageField(upload_to='images/post_images', verbose_name='Изображение статьи')),
                ('news_short_content', models.TextField(default='No short description', verbose_name='Кратко', max_length=500)),
                ('news_flickr_albumId', models.TextField(default='Нет фотографий', verbose_name='Flickr Album ID', max_length=300)),
                ('news_content', models.TextField(default='No content', verbose_name='Текст поста (максим 20000 симв)', max_length=20000)),
            ],
            options={
                'verbose_name': 'Новость',
                'verbose_name_plural': 'Новости',
                'ordering': ['-news_date'],
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('v_position', models.CharField(max_length=150)),
                ('v_requirements', models.CharField(max_length=1000)),
                ('v_duties', models.CharField(max_length=1000)),
                ('v_conditions', models.CharField(max_length=1000)),
                ('v_salary_from', models.CharField(default='По результатам ', max_length=100)),
                ('v_salary_to', models.CharField(default='собеседования', max_length=100)),
                ('v_actual', models.BooleanField(verbose_name='Актуальность вакансии')),
                ('v_added', models.DateTimeField(verbose_name='Датоа публикации')),
                ('v_company', models.ForeignKey(verbose_name='Работодатель:', to='home.Company', default='Частное лицо')),
            ],
            options={
                'verbose_name': 'Вакансия',
                'verbose_name_plural': 'Вакансии',
                'ordering': ['-v_added'],
            },
        ),
        migrations.CreateModel(
            name='UserFullName',
            fields=[
            ],
            options={
                'proxy': True,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='news_author',
            field=models.ForeignKey(verbose_name='Автор статьи', to='home.UserFullName', default='1'),
        ),
    ]
