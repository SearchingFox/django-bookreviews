from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Book


def home(request):
    searchTerm = request.GET.get("searchBook")
    if searchTerm:
        books = Book.objects.filter(title__icontains=searchTerm)
    else:
        books = Book.objects.all()
    return render(request, "home.html", {"searchTerm": searchTerm, "books": books})


def detail(request, book_id):
    movie = get_object_or_404(Book, pk=book_id)
    return render(request, "detail.html", {"movie": movie})


def signup(request):
    email = request.GET.get("email")
    return render(request, "signup.html", {"email": email})


def about(request):
    return HttpResponse("<h1>Welcome to About</h1>")
