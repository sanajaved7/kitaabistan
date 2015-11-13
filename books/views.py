from django.shortcuts import render, redirect
from .models import Book, Author
from .forms import BookForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'register.html', {'user_form': user_form, 'registered': registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('index')
            else:
                return HttpResponse("Account is disabled. Sorry!")
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse('Invalid login details supplied.')
    else:
        return render(request, 'login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

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
    books = Book.objects.filter(user=request.user.id)
    return render(request, 'index.html', context={'books':books, 'form':form})



@api_view(['GET'])
def book_collection(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def book_element(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return HttpResponse(status=400)

    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)
