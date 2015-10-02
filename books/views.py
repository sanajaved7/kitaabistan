from django.shortcuts import render
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', context={'books':books})
