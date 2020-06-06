from django.contrib import admin

from .models import Book, Author, Review, Genre


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'stock', 'book_cover')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'publish_date', 'text')


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Genre, GenreAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
