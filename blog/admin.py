from django.contrib import admin

from blog.models import Comment, Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "description", "tags")
    search_fields = ("title",)
    readonly_fields = ("created_at", "updated_at")
    # fieldsets eklenecek


admin.site.register(Comment)
