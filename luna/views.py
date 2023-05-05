from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import *
from .models import *
from .utils import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'}
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
        return Post.objects.filter(is_published=True)


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


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#     else:
#         form = AddPostForm()
#     return render(request, 'luna/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление книги'})


class ShowPost(DataMixin, DetailView):
    model = Post
    template_name = 'luna/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_contex(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


# def show_post(request, post_slug):
#     post = get_object_or_404(Post, slug=post_slug)
#
#     context = {'post': post,
#                'menu': menu,
#                'title': post.title,
#                'cat_selected': post.cat_id,
#                }
#     return render(request, 'luna/post.html', context=context)


class LunaCategory(DataMixin, ListView):
    model = Post
    template_name = 'luna/index.html'
    context_object_name = 'posts'
    allow_empty = False


    def get_queryset(self):
        return Post.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_contex(title='Категория - ' + str(context['posts'][0].cat),
                                     cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))


# def show_category(request, cat_slug):
#     posts = Post.objects.filter(cat_slug=cat_slug)
#     if len(posts) == 0:
#         raise Http404()
#     context = {'posts': posts,
#                'menu': menu,
#                'title': 'Категории',
#                'cat_selected': cat_slug,
#                }
#     return render(request, 'luna/index.html', context=context)


def login(request):
    return HttpResponse('Авторизация')


def contact(request):
    return HttpResponse('Контакты')


def categories(request, catid):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
