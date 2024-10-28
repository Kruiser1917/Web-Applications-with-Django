from django.urls import path
from .views import ProductListView, ProductCreateView, ProductUpdateView, ProductDeleteView, ContactView, ProductDetailView, unpublish_product, products_by_category

app_name = 'catalog'

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product_list'),
    path('products/create/', ProductCreateView.as_view(), name='product_create'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),  # Маршрут для детального просмотра продукта
    path('contact/', ContactView.as_view(), name='contact'),
    path('product/<int:pk>/unpublish/', unpublish_product, name='product_unpublish'),
    path('category/<int:category_id>/', products_by_category, name='products_by_category'),
]
