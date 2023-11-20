# control what do I want to view on my web page
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Book
from .forms import BookForm


# Create your views here.
def index(request):
    return HttpResponse("Hello World")


def homepage(request):
    return render(request, 'myapp/index.html')


def book(request):
    book_list = Book.objects.all()
    context = {
        'book_list': book_list
    }
    return render(request, 'myapp/books.html', context)


def detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'myapp/book.html', {
        'book': book
    })


def update(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'myapp/edit.html', {'form': form, 'book': book})


def add_book(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        price = request.POST.get('price', )
        image = request.FILES['image']
        book = Book(name=name, desc=desc, price=price, image=image)
        book.save()
    return render(request, 'myapp/add_book.html')


def delete(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html')
