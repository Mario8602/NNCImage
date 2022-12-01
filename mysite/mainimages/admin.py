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


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['post', 'user', 'body', 'created_date']
#     search_fields = ('author', 'post')


# class UserAdmin(admin.ModelAdmin):
#     list_display = ['email', 'username', "is_admin", "is_active"]
#     search_fields = ('username',)


admin.site.register(Post, PostAdmin)
# admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(GroupsPosts, GroupsPostsAdmin)
# admin.site.register(User, UserAdmin)


