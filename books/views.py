from django.shortcuts import render
from .models import Book, Author
from .forms import BookForm

def clean_author(new_author):
    new_author = new_author.split(" ")
    new_author = Author.objects.create(first_name=new_author[0], last_name=new_author[1])
    new_author.save()
    return new_author

def index(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():

            if form.cleaned_data['new_author'] != "":
                author = clean_author(form.cleaned_data['new_author'])
            else:
                author = form.cleaned_data['author']

            new_book = Book(
                title = form.cleaned_data['title'],
                genre = form.cleaned_data['genre'],
                owned = form.cleaned_data['owned'],
                to_read = form.cleaned_data['to_read'],
                author=author
            )
            new_book.save()
            form = BookForm()
    else:
        form = BookForm()
    books = Book.objects.all()
    return render(request, 'index.html', context={'books':books, 'form':form})
