from django.contrib import admin

from .models import Post, Category, GroupsPosts


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'body', 'photo', 'created_at', 'last_modified']
    search_fields = ('title', 'body')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'categories']
    search_fields = ('categories',)


class GroupsPostsAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'cover', 'body', 'is_private']
    search_fields = ('title',)


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(GroupsPosts, GroupsPostsAdmin)
