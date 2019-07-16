from django.shortcuts import render


# Create your views here.
def index(request):

    return render(request, "index.html")

def bookss(request):

    return render(request, "store-books.html")