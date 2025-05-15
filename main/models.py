from django.db import models
from django.utils.text import slugify

class HomePage(models.Model):
    hero_title = models.CharField(max_length=255)
    hero_subtitle = models.TextField()

    def __str__(self):
        return "Homepage Content"

class FeaturedBook(models.Model):
    homepage = models.ForeignKey(HomePage, on_delete=models.CASCADE, related_name='featured_books')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='featured_books/')

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='books/')
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    body = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='gallery/')
    description = models.TextField(default="No description")
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Popup(models.Model):
    image = models.ImageField(upload_to='popup/')
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
