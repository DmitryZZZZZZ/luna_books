from django.db.models import Count

from luna.models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить книгу', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        ]


class DataMixin:
    paginate_by = 5

    def get_user_contex(self, **kqargs):
        context = kqargs
        cats = Category.objects.annotate(Count('post'))
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)
        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context