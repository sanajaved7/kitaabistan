from django.shortcuts import render
from .models import Book
from .forms import BookForm

def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            form = BookForm()
    else:
        form = BookForm()
    books = Book.objects.all()
    return render(request, 'index.html', context={'books':books, 'form':form})
