from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Черновик'),
        ('published', 'Публикация'),
    )
    # title - это поле заголовка статьи. Оппределенно как CharField - VARCHAR для БД
    title = models.CharField(max_length=250)
    # slug - это поле будет использоватся для формирования URL. Слаг - короткое название,
    # содержащее только буквы, цифры и нижнее подчеркивания или дефисы. Unique_for_data -
    # парвметр с помощью которого мы сможем формировать уникальные URL используя дату публикации
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # author - является внешним ключем иопределяет отношение один ко многим
    # тоесть у автора может быть множество статей но, у статьи только один автор
    # on_delete - при удалении пользователя, удаляем и его посты
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    # body - тело статьи
    body = models.TextField()
    # publish - возвращает текущую дату и время. Можно рассматривать как стандартную функцию datatime.now
    publish = models.DateTimeField(default=timezone.now)
    # created - с помощью auto_add_now мы указываем дату автоматически при создании объекта.
    created = models.DateTimeField(auto_now_add=True)
    # update - дата  и время которые указывают на то, когда статья была отредактирована
    # auto_now - сохраняет дату при сохранении объекта
    update = models.DateTimeField(auto_now=True)
    # status - статус статьи
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Черновик')


class Meta:
    ordering = ('-publish',)


def __str__(self):
    return self.title
