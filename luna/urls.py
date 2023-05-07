from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    path('', cache_page(60)(LunaHome.as_view()), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('success_send/', success, name='success'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', SignupView.as_view(), name='register'),
    path('logout/', LogoutView.as_view() , name='logout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', LunaCategory.as_view(), name='category'),
]