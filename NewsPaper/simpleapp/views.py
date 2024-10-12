# Импортируем класс, который говорит нам о том,
# что в этом представлении мы будем выводить список объектов из БД
from datetime import datetime
from django.views.generic import ListView, DetailView
from .models import News
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django_filters.views import FilterView
from .filters import NewsFilter
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import NewsForm



class NewsListView(ListView):
    model = News
    template_name = 'news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10

    def get_queryset(self):
        return News.objects.all().order_by('-publication_date')


class NewsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = News
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-publication_date'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news_list.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news_list'



    def news_detail(request, news_id):
        news_item = get_object_or_404(News, id=news_id)
        return render(request, 'one_news.html', {'news_item': news_item})

    def get_context_data(self, **kwargs):
        # С помощью super() мы обращаемся к родительским классам
        # и вызываем у них метод get_context_data с теми же аргументами,
        # что и были переданы нам.
        # В ответе мы должны получить словарь.
        context = super().get_context_data(**kwargs)
        # К словарю добавим текущую дату в ключ 'time_now'.
        context['time_now'] = datetime.utcnow()
        # Добавим ещё одну пустую переменную,
        # чтобы на её примере рассмотреть работу ещё одного фильтра.
        context['next_sale'] = None
        return context

class NewsDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельной новости
    model = News
    # Используем другой шаблон — product.html
    template_name = 'one_news.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'one_news'

class NewsSearchView(FilterView):
    model = News
    template_name = 'news_search.html'
    filterset_class = NewsFilter

class NewsCreateView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news_form.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        news = form.save(commit=False)
        news.type = 'новость'
        return super().form_valid(form)

class ArticleCreateView(CreateView):
    model = News
    form_class = NewsForm
    template_name = 'news_form.html'
    success_url = reverse_lazy('news_list')

    def form_valid(self, form):
        article = form.save(commit=False)
        article.type = 'статья'
        return super().form_valid(form)

class NewsUpdateView(UpdateView):
    model = News
    form_class = NewsForm
    template_name = 'news_form.html'
    success_url = reverse_lazy('news_list')

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'news_confirm_delete.html'
    success_url = reverse_lazy('news_list')