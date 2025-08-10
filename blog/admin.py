from django.contrib import admin
from blog.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    # Поля, которые будут отображаться в списке записей
    list_display = (
        'title',
        'created_at',
        'is_published',
        'views_count',
        'preview_thumbnail'
    )

    # Поле для поиска
    search_fields = ('title', 'content')

    # Фильтрация
    list_filter = ('is_published', 'created_at')

    # Поля для редактирования прямо в списке
    list_editable = ('is_published',)

    # Сортировка по умолчанию
    ordering = ('-created_at',)

    # Поля для отображения в форме редактирования
    fieldsets = (
        (None, {
            'fields': ('title', 'preview', 'content')
        }),
        ('Публикация', {
            'fields': ('is_published',)
        }),
        ('Дополнительно', {
            'fields': ('views_count',),
            'classes': ('collapse',)
        })
    )

    # Метод для отображения миниатюры превью
    def preview_thumbnail(self, obj):
        if obj.preview:
            return f'<img src="{obj.preview.url}" width="100" height="100">'
        return 'Нет изображения'

    preview_thumbnail.allow_tags = True
    preview_thumbnail.short_description = 'Превью'


admin.site.register(BlogPost, BlogPostAdmin)
