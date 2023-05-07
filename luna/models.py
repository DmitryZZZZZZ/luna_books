from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст')
    author = models.TextField(blank=True, verbose_name='Автор')
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    year_of_publishing = models.IntegerField(blank=True, verbose_name='Год издания')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    url = models.URLField(blank=True, verbose_name='Ссылка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=80, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})


class Contact(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    email = models.EmailField(max_length=200)
    message = models.TextField(max_length=1000, verbose_name='Сообщение')

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('contact')
