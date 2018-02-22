from django.contrib import admin
from .models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'content', 'pub')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('blog', 'name', 'content', 'pub')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)