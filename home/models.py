from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class UserFullName(User):
    class Meta:
        proxy = True

    def __unicode__(self):
        return self.get_full_name()

class Company(models.Model):
    company_type = models.CharField(max_length=100, verbose_name=u'Форма собственности')
    company_name = models.CharField(max_length=150, verbose_name=u'Нименование организации')
    slug = models.SlugField(max_length=255, verbose_name=u'Идентификатор', unique=True)
    company_address = models.TextField(max_length=400, verbose_name=u'Адрес организации')
    company_phone = models.CharField(max_length=100, verbose_name=u'Контактные телефоны')
    company_contactPerson = models.CharField(max_length=100, verbose_name=u'Контактное лицо компании')
    company_email = models.CharField(max_length=50, verbose_name=u'Электронная почта')
    company_about = models.TextField(max_length=1000, verbose_name=u'Информация об организации')

    class Meta:
        ordering = ['-company_name', ]
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return '/company/%s/' % self.slug

class Vacancy(models.Model):
    v_position = models.CharField(max_length=150)
    v_requirements = models.TextField(max_length=1000)
    v_duties = models.TextField(max_length=1000)
    v_conditions = models.TextField(max_length=1000)
    v_salary_from = models.CharField(max_length=100, default="По результатам ")
    v_salary_to = models.CharField(max_length=100, default="собеседования")
    v_actual = models.BooleanField(u'Актуальность вакансии')
    v_added = models.DateTimeField(u'Дата публикации')
    v_company = models.ForeignKey(Company, default="Частное лицо", verbose_name="Работодатель:")

    class Meta:
        ordering = ['-v_added', ]
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

class News(models.Model):
    news_title = models.CharField(max_length=255, verbose_name="Заголовок поста")   # 3аголовок поста
    slug = models.SlugField(max_length=255, verbose_name="Идентификатор")    # Slug
    news_date = models.DateTimeField(u'Дата публикации')    # дата публикации u'Дата публикации'
    news_image = models.ImageField(upload_to='images/post_images', verbose_name="Изображение статьи")
    news_content = models.TextField(default="No content",
                                    verbose_name="Текст поста (максим 20000 симв)")   # текст поста
    flickr_album = models.TextField(max_length=1000, default="Нет фотографий", verbose_name="Код альбома для вставки")

    news_author = models.ForeignKey(User, default='1', verbose_name="Автор статьи")   # Автор поста

    class Meta:
        ordering = ['-news_date', ]
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return "/news/%s/" % self.slug

class Announcements(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок поста")   # 3аголовок поста
    slug = models.SlugField(max_length=255, verbose_name="Идентификатор")    # Slug
    date = models.DateTimeField(u'Дата публикации')    # дата публикации u'Дата публикации'
    image = models.ImageField(upload_to='images/post_images', verbose_name="Изображение статьи")
    content = models.TextField(max_length=10000,
                                    default="No content",
                                    verbose_name="Текст поста (максим 10000 симв)")   # текст поста
    author = models.ForeignKey(UserFullName, default='1', verbose_name="Автор статьи")   # Автор поста

    class Meta:
        ordering = ['-date', ]
        verbose_name = 'Анонс'
        verbose_name_plural = 'Анонсы'

    def __unicode__(self):
        return self.slug

    def get_absolute_url(self):
        return "/announcements/%s/" % self.slug

class Main(models.Model):
    news = models.ForeignKey(News, verbose_name="Новости")
    vacancy = models.ForeignKey(Vacancy, verbose_name="Вакансии")
    announce = models.ForeignKey(Announcements, verbose_name="Анонсы")

