from django.shortcuts import render

from .models import Book

# Create your views here.
def index(request):

    return render(request, "index.html")

def store(request):
    count=Book.objects.all().count()
    context ={
        'count': count,
    }
    return render(request, "store-books.html", context)