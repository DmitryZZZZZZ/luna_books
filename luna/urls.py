from django.urls import path

from .views import *

urlpatterns = [
    path('', LunaHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', SignupView.as_view(), name='register'),
    path('logout/', LogoutView.as_view() , name='logout'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', LunaCategory.as_view(), name='category'),
]