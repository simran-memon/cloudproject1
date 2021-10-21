"""aws_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from s3_app import views
from users import views as user_views


urlpatterns = [
    path('home/', views.Home.as_view(), name='home'),
    path('', views.Home.as_view(), name='home'),
    #path('', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    #path('upload_file/', views.upload, name='upload_file'),
    path('files/', views.list_objects, name='list_objects'),
    path('files/upload/', views.upload_file, name='upload_file'),
    path('files/update/<int:pk>/', views.update_file, name='update_file'),
    path('files/<int:pk>/', views.delete_file, name='delete_file'),
    path('buckets/', views.list_buckets, name='list_buckets'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('admin_login/', auth_views.LoginView.as_view(template_name='admin_login.html'), name='admin_login'),


    #path('class/books/', views.BookListView.as_view(), name='class_book_list'),
    #path('class/books/upload/', views.UploadBookView.as_view(), name='class_upload_book'),
    path('admin/', admin.site.urls),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

