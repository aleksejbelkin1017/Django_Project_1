from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = "Add test products to the database"

    def handle(self, *args, **kwargs):
        # Удаляем все объекты из базы данных
        from catalog.models import Product

        Product.objects.all().delete()

        # Загружаем данные из фикстуры
        call_command("loaddata", "catalog.json")

        self.stdout.write(
            self.style.SUCCESS("Тестовые продукты успешно добавлены из фикстуры.")
        )
