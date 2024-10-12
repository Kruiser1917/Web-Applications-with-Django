from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from catalog.views import HomeView  # Импортируем HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),  # Используем HomeView для главной страницы
    path('catalog/', include('catalog.urls', namespace='catalog')),
    path('blog/', include('blog.urls')),  # Подключение маршрутов для блога
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)