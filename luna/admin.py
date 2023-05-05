from django.contrib import admin
from luna.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'year_of_publishing', 'cat', 'time_create', 'photo', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content', 'author', 'year_of_publishing')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create', 'author', 'year_of_publishing')
    prepopulated_fields = {'slug': ('title',)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)