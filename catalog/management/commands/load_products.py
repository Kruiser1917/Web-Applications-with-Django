from catalog.models import Category, Product
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Заполнение базы данных тестовыми данными'

    def handle(self, *args, **kwargs):
        # Создаем категорию, если она не существует
        category, created = Category.objects.get_or_create(
            name='Электроника',
            defaults={'description': 'Электронные устройства'}
        )

        # Теперь создаем продукты
        Product.objects.create(
            name='Смартфон',
            description='Лучший смартфон на рынке',
            price=19999.99,
            category=category
        )
        Product.objects.create(
            name='Ноутбук',
            description='Высокопроизводительный ноутбук',
            price=79999.99,
            category=category
        )

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена тестовыми данными.'))
