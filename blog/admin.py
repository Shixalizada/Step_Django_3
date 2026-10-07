from django.contrib import admin

from .models import Category, Post


@admin.action(description="Seçilmiş et")
def make_featured(modeladmin, request, queryset):
    queryset.update(is_featured=True)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "is_published", "is_featured", "views"]
    list_editable = ["is_published", "is_featured"]
    list_filter = ["is_published", "is_featured", "category", "created_at"]
    search_fields = ["title", "content", "author"]
    actions = [make_featured]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    search_fields = ["name", "slug"]
