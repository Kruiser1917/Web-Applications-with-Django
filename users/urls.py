from django.urls import path
from .views import register, login_view
from django.urls import include, path

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('users/', include('users.urls')),
]
