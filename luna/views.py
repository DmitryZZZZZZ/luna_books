from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.core.paginator import Paginator
from allauth.account.views import LoginView, SignupView, LogoutView, email
from django.core.mail import EmailMessage

from PyDev.settings import DEFAULT_FROM_EMAIL
from .forms import *
from .models import *
from .utils import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить книгу', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        ]


class LunaHome(DataMixin, ListView):
    model = Post
    template_name = 'luna/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)  # словарь ListView
        c_def = self.get_user_contex(title='Главная страница')  # словарь DataMixin
        return dict(list(context.items()) + list(c_def.items()))  # объединяю словари

    def get_queryset(self):
        return Post.objects.filter(is_published=True).select_related('cat')


def about(request):
    return render(request, 'luna/about.html', {'menu': menu, 'title': 'О сайте'})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'luna/addpage.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_contex(title='Добавление книги')
        return dict(list(context.items()) + list(c_def.items()))


class ShowPost(DataMixin, DetailView):
    model = Post
    template_name = 'luna/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_contex(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class LunaCategory(DataMixin, ListView):
    model = Post
    template_name = 'luna/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_contex(title='Категория - ' + str(c.name), cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


class ContactFormView(DataMixin, CreateView):
    form_class = ContactForm
    template_name = 'luna/contact.html'
    success_url = reverse_lazy('success')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_contex(title='Обратная связь')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        data = form.cleaned_data
        subject = f'Заполнена форма обратной связи luna-books от {data["first_name"]} {data["last_name"]}' \
                  f' Почта отправителя: {data["email"]}'
        message = data.get('message')
        send_mail(subject, message, '', [DEFAULT_FROM_EMAIL], fail_silently=False)
        return super().form_valid(form)


def success(request):
    return render(request, 'luna/success_send_mail.html')


def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
