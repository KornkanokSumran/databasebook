from django.contrib import admin
from .models import Book, Publisher, Author
# Register your models here.
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(Author)
