from django.contrib import admin
from . models import Book, Author, Rate
# Register your models here.


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Rate)
