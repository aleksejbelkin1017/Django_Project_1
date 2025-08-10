from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок'
    )

    preview = models.ImageField(
        upload_to='blog/image',
        null=True,
        blank=True,
        verbose_name='Превью'
    )

    content = models.TextField(
        verbose_name='Содержимое'
    )

    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата создания'
    )

    is_published = models.BooleanField(
        default=False,
        verbose_name='Признак публикации'
    )

    views_count = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество просмотров'
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Запись блога'
        verbose_name_plural = 'Записи блога'
        ordering = ['-created_at']
