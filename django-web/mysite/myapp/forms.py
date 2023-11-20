from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    # meta class which holds information about class itself
    class Meta:
        model = Book
        fields = ['name', 'desc', 'price', 'image']
