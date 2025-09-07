from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from .models import *

def index(request):
    books = Book.objects.all().order_by("title")
    num_books = books.count()
    avg_books = books.aggregate(Avg("rating"))
    return render(request, "book_outlet/index.html", { "books": books, "total_number_books": num_books, "average_rating": avg_books})

def book_detail(request, id, slug):
    book = get_object_or_404(Book, id=id)
    return render(request, "book_outlet/book_detail.html", { "book": book })