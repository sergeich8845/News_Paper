from django.contrib.auth.models import User
from news.models import Author, Category, Post, Comment

# Создать двух пользователей
user1 = User.objects.create_user('user1')
user2 = User.objects.create_user('user2')

# Создать два объекта модели Author, связанные с пользователями
author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

# Добавить 4 категории в модель Category
category1 = Category.objects.create(name='Спорт')
category2 = Category.objects.create(name='Политика')
category3 = Category.objects.create(name='Образование')
category4 = Category.objects.create(name='Технологии')

# Добавить 2 статьи и 1 новость
post1 = Post.objects.create(author=author1, type=Post.ARTICLE, title='Статья 1', content='Контент статьи 1')
post2 = Post.objects.create(author=author2, type=Post.ARTICLE, title='Статья 2', content='Контент статьи 2')
news1 = Post.objects.create(author=author1, type=Post.NEWS, title='Новость 1', content='Контент новости 1')

# Присвоить им категории
post1.categories.add(category1, category2)
post2.categories.add(category3)
news1.categories.add(category4, category1)

# Создать как минимум 4 комментария к разным объектам модели Post
comment1 = Comment.objects.create(post=post1, user=user2, content='Комментарий к статье 1')
comment2 = Comment.objects.create(post=post2, user=user1, content='Комментарий к статье 2')
comment3 = Comment.objects.create(post=news1, user=user2, content='Комментарий к новости 1')
comment4 = Comment.objects.create(post=post1, user=user1, content='Ещё один комментарий к статье 1')

# Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов
post1.like()
post1.like()
post2.like()
news1.dislike()
comment1.like()
comment2.dislike()
comment3.like()
comment3.like()
comment4.dislike()

# Обновить рейтинги пользователей
author1.update_rating()
author2.update_rating()

#Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта)
# Находим лучшего пользователя по рейтингу
best_author = Author.objects.order_by('-rating').first()

# Выводим username и рейтинг лучшего пользователя
print(f"Лучший пользователь: {best_author.user.username}, Рейтинг: {best_author.rating}")

#Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье
# Находим лучшую статью по рейтингу
best_post = Post.objects.order_by('-rating').first()

# Выводим дату добавления, username автора, рейтинг, заголовок и превью
print(f"Дата добавления: {best_post.created_at}")
print(f"Автор: {best_post.author.user.username}")
print(f"Рейтинг: {best_post.rating}")
print(f"Заголовок: {best_post.title}")
print(f"Превью: {best_post.preview()}")

#Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье
# Находим все комментарии к лучшей статье
comments = Comment.objects.filter(post=best_post)

# Выводим дату, пользователя, рейтинг и текст каждого комментария
for comment in comments:
    print(f"Дата: {comment.created_at}")
    print(f"Пользователь: {comment.user.username}")
    print(f"Рейтинг: {comment.rating}")
    print(f"Текст: {comment.content}")
    print()  # Пустая строка для разделения комментариев