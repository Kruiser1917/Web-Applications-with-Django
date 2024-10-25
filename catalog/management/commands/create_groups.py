from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу "Модератор продуктов" с нужными правами'

    def handle(self, *args, **options):
        # Создаем группу "Модератор продуктов"
        moderator_group, created = Group.objects.get_or_create(name="Модератор продуктов")

        # Добавляем права группе
        can_unpublish = Permission.objects.get(codename='can_unpublish_product')
        can_delete = Permission.objects.get(codename='delete_product')
        moderator_group.permissions.add(can_unpublish, can_delete)

        self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" успешно создана с нужными правами'))
