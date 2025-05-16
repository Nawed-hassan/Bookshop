from django.contrib import admin
from django.urls import path
from main import views  # import views from your 'main' app

urlpatterns = [
    
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('books/', views.books, name='books'),
    path('blog/', views.blog, name='blog'),
    path('books/<slug:slug>/', views.book_detail, name='book_detail'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('gallery/<slug:slug>/', views.gallery_detail, name='gallery_detail')
]
