from django.urls import path, include 
from . import views
from django.views.generic import TemplateView

# Для выгрузки фото
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    
    path('', views.index, name='index'),
    path('tinymce/', include('tinymce.urls')), 
    path('info', views.info, name='info'),
    path('project', views.project, name='project'),
    path('addproject', views.add_project, name="add_project"),
    path('catalog_book/<int:pk>', views.book_detail, name="book-detail"),
    path('logout', views.logout_view, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)