from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import Book, Author

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class BookForm(forms.Form):
    """ Creates a form with the fields from the Book
    model. """
    title = forms.CharField(label="Title", max_length=100)
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label="Existing Authors", required=False)
    new_author = forms.CharField(label="New Author", max_length=100, required=False)
    genre = forms.CharField(label="Genre", max_length=75)
    owned = forms.BooleanField(label="Do you own this book?", required=False)
    to_read = forms.BooleanField(label="Do you want to read this book?", required=False)
