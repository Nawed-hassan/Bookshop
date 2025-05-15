from django.shortcuts import render, get_object_or_404
from .models import HomePage, FeaturedBook, Book, Gallery, Blog

def index(request):
    content = HomePage.objects.first()
    featured_books = FeaturedBook.objects.filter(homepage=content) if content else []
    return render(request, 'home.html', {
        'content': content,
        'featured_books': featured_books,
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def gallery(request):
    images = Gallery.objects.all()
    return render(request, 'gallery.html', {'images': images})

def gallery_detail(request, slug):
    image = get_object_or_404(Gallery, slug=slug)
    return render(request, 'gallery_detail.html', {'image': image})

def books(request):
    all_books = Book.objects.all()
    return render(request, 'books.html', {'all_books': all_books})

def book_detail(request, slug):
    book = get_object_or_404(Book, slug=slug)
    return render(request, 'book_detail.html', {'book': book})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})

def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_detail.html', {'post': post})
