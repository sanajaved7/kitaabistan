from django.forms import ModelForm
from .models import Book

class BookForm(ModelForm):
    """ Creates a form with the fields from the Book
    model. """
    class Meta:
        model = Book
        fields = "__all__"
