from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blogpage ,name="blogpage"),
    path('blogpost', views.blogpost, name="blogpost"),
    path('<slug:slug>/', views.blogpost, name='blogpost'),
    
]
