from django.urls import path
from . import views
from django.views.generic import TemplateView

# Для выгрузки фото
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    
    path('', views.index, name='index'),
    path('catalog_book', views.catalog_book, name='catalog_book'),
    path('catalog_book/<int:pk>', views.book_detail, name="book-detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)