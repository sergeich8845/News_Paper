from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


# Пост
class News(models.Model):
    title = models.CharField(max_length=200, unique=True)
    publication_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
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