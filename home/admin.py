from django.contrib import admin
from home.models import Company, News, Vacancy, Announcements, Main


class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('company_name',)}

    class Media:
        js = ('/static/tinymce/tiny_mce.js',
              '/static/tinymce/tiny_mce_init.js',
         )

class VacancyAdmin(admin.ModelAdmin):
     class Media:
        js = ('/static/tinymce/tiny_mce.js',
              '/static/tinymce/tiny_mce_init.js',
         )

class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('news_title',)}
    class Media:
        js = ('/static/tinymce/tiny_mce.js',
              '/static/tinymce/tiny_mce_init.js',
         )

class AnnouncementsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    class Media:
        js = ('/static/tinymce/tiny_mce.js',
              '/static/tinymce/tiny_mce_init.js',
         )

class MainAdmin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Announcements, AnnouncementsAdmin)
admin.site.register(Main, MainAdmin)