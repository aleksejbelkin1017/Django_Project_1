from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Создаёт группы пользователей: Модератор продуктов, Контент-менеджер"

    def handle(self, *args, **options):
        self._create_moderators_group()
        self._create_content_managers_group()
        self.stdout.write(self.style.SUCCESS("Группы успешно созданы / обновлены"))

    def _create_moderators_group(self):
        group, created = Group.objects.get_or_create(name="Модератор продуктов")

        # Кастомное право на отмену публикации (объявлено в Meta модели Product)
        can_unpublish = Permission.objects.get(
            codename="can_unpublish_product",
            content_type__app_label="catalog",
        )
        # Стандартное право на удаление продукта (создаётся Django автоматически)
        can_delete = Permission.objects.get(
            codename="delete_product",
            content_type__app_label="catalog",
        )

        group.permissions.set([can_unpublish, can_delete])

        action = "создана" if created else "обновлена"
        self.stdout.write(f"Группа «Модератор продуктов» {action}")

    def _create_content_managers_group(self):
        group, created = Group.objects.get_or_create(name="Контент-менеджер")

        # Права на CRUD блога
        codenames = [
            "add_blogpost",
            "change_blogpost",
            "delete_blogpost",
            "view_blogpost",
        ]
        permissions = Permission.objects.filter(
            codename__in=codenames,
            content_type__app_label="blog",
        )

        group.permissions.set(permissions)

        action = "создана" if created else "обновлена"
        self.stdout.write(f"Группа «Контент-менеджер» {action}")
