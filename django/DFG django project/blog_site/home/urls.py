from django.contrib import admin
from django.urls import path
from django.urls import include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about', views.about,name='about'),
    path('contact', views.contact,name='contact'),
    path('', views.home,name = 'home'),
    path('search', views.search, name='search')
]