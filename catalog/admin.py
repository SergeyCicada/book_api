from django.contrib import admin

from catalog.models import Book, Genre, Language, Author

admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(Author)
