from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from .views import BaseRegisterView
from django.urls import path
from django.contrib import admin
# Импортируем созданное нами представление
from .views import (NewsList, NewsListView, NewsDetail,
    NewsCreateView, ArticleCreateView, NewsUpdateView, NewsDeleteView,
    NewsSearchView, IndexView, upgrade_me
)



urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем новостям у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   # pk — это первичный ключ новости, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('news/<int:pk>', NewsDetail.as_view()),
   path('news/', NewsListView.as_view(), name='news_list'),
   path('news/create/', NewsCreateView.as_view(), name='news_create'),
   path('news/<int:pk>/edit/', NewsUpdateView.as_view(), name='news_edit'),
   path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
   path('articles/create/', ArticleCreateView.as_view(), name='article_create'),
   path('articles/<int:pk>/edit/', NewsUpdateView.as_view(), name='article_edit'),
   path('articles/<int:pk>/delete/', NewsDeleteView.as_view(), name='article_delete'),
   path('news/search/', NewsSearchView.as_view(), name='news_search'),
   path('index/', IndexView.as_view(template_name = 'account/index.html')),
   path('login/',
         LoginView.as_view(template_name = 'account/login.html'),
         name='login'),
   path('logout/',
         LogoutView.as_view(template_name = 'account/logout.html'),
         name='logout'),
   path('signup/',
         BaseRegisterView.as_view(template_name = 'account/signup.html'),
         name='signup'),
   path('upgrade/', upgrade_me, name = 'upgrade')
]