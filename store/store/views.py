from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.views import generic

from .models import Book, BookOrder, Cart, Review, Genre


# Create your views here.
class StoreView(generic.ListView):
    template_name = "base.html"
    context_object_name = 'books'  # your own name for the list as a template variable
    queryset = Book.objects.all()
    model = Book

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(StoreView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['books'] = self.model.objects.all()
        return context


# def store(request):
#     books = Book.objects.all()
#     context = {
#         'books': books,
#     }
#     return render(request, "base.html", context)


def book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    genre = Genre.objects.all()
    context = {
        'book': book,
        'genres': genre
    }
    return render(request, 'store/detail.html', context)


def add_to_cart(request, book_id):
    if request.user.is_authenticated:
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            pass

        else:
            try:
                cart = Cart.objects.get(user=request.user, active=True)
            except ObjectDoesNotExist:
                cart = Cart.objects.create(
                    user=request.user
                )
                cart.save()
            cart.add_to_cart(book_id)
        return redirect('cart')
    else:
        return redirect('index')


def remove_from_cart(request, book_id):
    if request.user.is_authenticated:
        try:
            book = Book.objects.get(pk=book_id)
        except ObjectDoesNotExist:
            pass

        else:
            cart = Cart.objects.get(user=request.user, active=True)
            cart.remove_from_cart(book_id)
        return redirect('cart')
    else:
        return redirect('index')


def cart(request):
    if request.user.is_authenticated:
        cart = Cart.objects.get(user=request.user, active=True)
        orders = BookOrder.objects.filter(cart=cart)
        total = 0
        count = 0
        for order in orders:
            total += (order.book.price * order.quantity)
            count += order.quantity
        context = {
            'cart': orders,
            'total': total,
            'count': count,
        }
        return render(request, 'store/cart.html', context)
    else:
        return redirect('index')
