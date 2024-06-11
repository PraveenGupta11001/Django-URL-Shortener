# urls.py
from django.urls import path
from .views import url_shorten_view, redirect_view

urlpatterns = [
    path('', url_shorten_view, name='url_shorten'),
    path('<str:token>/', redirect_view, name='redirect'),
]