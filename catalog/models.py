from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=150, verbose_name="Наименование", help_text="Наименование категории"
    )
    description = models.TextField(
        verbose_name="Описание", help_text="Описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
        help_text="Введите описание продукта",
    )
    image = models.ImageField(
        upload_to="catalog/image",
        null=True,
        blank=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку", help_text="Введите цену за покупку"
    )
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    update_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "price"]

    def __str__(self):
        return self.name
