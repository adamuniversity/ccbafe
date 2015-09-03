from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from home.models import News, Vacancy, Company, Announcements

def index(request):
    return render_to_response('home/index.html', context_instance=RequestContext(request))

class NewsListView(ListView):
    template_name = 'home/news/news_list.html'
    model = News
    paginate_by = 3
    queryset = News.objects.all()
    context_object_name = 'news_list'

class NewsDetailView(DetailView): #детализированное представление модели
    template_name = 'home/news/news_details.html'
    context_object_name = 'news'
    model = News

# ******************************************************************

class VacancyListView(ListView):
    template_name = 'home/vacancy/vacancy_list.html'
    model = Vacancy
    paginate_by = 3
    queryset = Vacancy.objects.all()
    context_object_name = 'vacancy_list'

class VacancyDetailView(DetailView): #детализированное представление модели
    template_name = 'home/vacancy/vacancy_details.html'
    context_object_name = 'vacancies'
    model = Vacancy


# ******************************************************************

class AnnouncementsListView(ListView):
    template_name = 'home/announce/announce_list.html'
    model = Announcements
    paginate_by = 3
    queryset = Announcements.objects.all()
    context_object_name = 'ann_list'

class AnnouncementsDetailView(DetailView): #детализированное представление модели
    template_name = 'home/announce/announce_detail.html'
    context_object_name = 'announcement'
    model = Announcements
