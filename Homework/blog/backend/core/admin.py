from django.contrib import admin

from .models import Post, Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ("text",)
    list_filter = ("author", "post")
    list_display = ("__str__", "author", "post")


class CommentInline(admin.TabularInline):
    model = Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ("title",)
    list_filter = ("author",)
    inlines = (CommentInline,)