from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.utils import timezone
from django.core.validators import MinValueValidator


# Пост
class News(models.Model):
    TYPE_CHOICES = [
        ('новость', 'Новость'),
        ('статья', 'Статья'),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100, blank=True, null=True)
    publication_date = models.DateField()
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, default='новость')


    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE, null=True, blank=True,
        related_name='news', # все новости в категории будут доступны через поле news
    )

    def __str__(self):
        return f'{self.title.title()}: {self.content}'





# Категория, к которой будет привязываться новость
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username",
                  "first_name",
                  "last_name",
                  "email",
                  "password1",
                  "password2", )
