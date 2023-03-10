from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Book, Review
from .forms import ReviewForm


def home(request):
    searchTerm = request.GET.get("searchBook")
    if searchTerm:
        books = Book.objects.filter(title__icontains=searchTerm)
    else:
        books = Book.objects.all()
    return render(request, "home.html", {"searchTerm": searchTerm, "books": books})


def detail(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, "detail.html", {"book": book})


def createreview(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == "GET":
        return render(
            request, "createreview.html", {"form": ReviewForm(), "book": book}
        )
    else:
        try:
            form = ReviewForm(request.POST)
            newReview = form.save(commit=False)
            newReview.user = request.user
            newReview.book = book
            newReview.save()
            return redirect("detail", newReview.book.id)
        except ValueError:
            return render(
                request,
                "createreview.html",
                {"form": ReviewForm(), "error": "bad data passed in"},
            )


def signup(request):
    email = request.GET.get("email")
    return render(request, "signup.html", {"email": email})


def about(request):
    return HttpResponse("<h1>Welcome to About</h1>")
