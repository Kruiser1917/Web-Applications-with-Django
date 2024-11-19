# catalog/services.py

from django.core.cache import cache
from .models import Product

def get_products_by_category(category_id):
    """
    Возвращает список продуктов в указанной категории с использованием кеширования.
    Кеширует данные на 10 минут.
    """
    cache_key = f'products_by_category_{category_id}'
    products = cache.get(cache_key)

    if not products:
        # Если данные не найдены в кеше, запросите их из базы данных
        products = list(Product.objects.filter(category_id=category_id, is_published=True))
        # Сохраните в кеш на 10 минут
        cache.set(cache_key, products, 60 * 10)

    return products

def unpublish_product(product):
    """
    Отменяет публикацию продукта.
    Устанавливает флаг is_published в False и сохраняет изменения.
    """
    product.is_published = False
    product.save()
