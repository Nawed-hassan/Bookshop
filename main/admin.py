from django.contrib import admin
from .models import Book, Blog, Gallery, Popup, HomePage

@admin.register(HomePage)
class HomePageAdmin(admin.ModelAdmin):
    list_display = ['hero_title']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'image', 'description', 'slug')
    search_fields = ('title', 'category', 'description')
    list_filter = ('category',)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'slug')
    search_fields = ('title', 'date')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image', 'slug')  # Added slug field
    search_fields = ('title', 'description')
    list_filter = ('title',)


@admin.register(Popup)
class PopupAdmin(admin.ModelAdmin):
    list_display = ('text', 'image')  # Display fields for Popup model
    search_fields = ('text',)
