from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return '%s, %s' % (self.last_name, self.first_name)


class Genre(models.Model):
    name = models.CharField(
        max_length=200,
        help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)"
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, )
    description = models.TextField()
    publish_date = models.DateField(default=timezone.now)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    stock = models.IntegerField(default=0)
    book_cover = models.ImageField(upload_to='img/', default='empty_cover.jpg',)
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")

    def __str__(self):
        return '%s' % self.title

    def display_genre(self):
        return ', '.join([genre.name for genre in self.genre.all()[:3]])

    display_genre.short_description = 'Genre'


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    publish_date = models.DateField(default=timezone.now)
    text = models.TextField()

    def __str__(self):
        return '%s' % self.text


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, )
    active = models.BooleanField(default=True)
    order_date = models.DateField(null=True)
    payment_type = models.CharField(max_length=100, null=True)
    payment_id = models.CharField(max_length=100, null=True)

    def add_to_cart(self, book_id):
        book = Book.objects.get(pk=book_id)
        try:
            preexisting_order = BookOrder.objects.get(book=book, cart=self)
            preexisting_order.quantity += 1
            preexisting_order.save()
        except BookOrder.DoesNotExist:
            new_order = BookOrder.objects.create(
                book=book,
                cart=self,
                quantity=1
            )
            new_order.save()

    def remove_from_cart(self, book_id):
        book = Book.objects.get(pk=book_id)
        try:
            preexisting_order = BookOrder.objects.get(book=book, cart=self)
            if preexisting_order.quantity > 1:
                preexisting_order.quantity -= 1
                preexisting_order.save()
            else:
                preexisting_order.delete()
        except BookOrder.DoesNotExist:
            pass


class BookOrder(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, )
    quantity = models.IntegerField()

