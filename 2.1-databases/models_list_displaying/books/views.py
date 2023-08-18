from django.http import HttpResponse
from django.shortcuts import render
from books.models import Book

def books_view(request):
    template = 'books/books_list.html'
    context = {
        'books': Book.objects.all()
    }
    return render(request, template, context)

def book_view(request, pub_date):
    template = 'books/book.html'
    previous_dated = Book.objects.filter(pub_date__lt=pub_date)
    next_dated = Book.objects.filter(pub_date__gt=pub_date)
    context = {
        'books': Book.objects.filter(pub_date=pub_date),
        'next_date': next_dated[0].pub_date.strftime('%Y-%m-%d') if next_dated else 'Каталог',
        'previous_date': previous_dated[0].pub_date.strftime('%Y-%m-%d') if previous_dated else 'Каталог',
    }
    return render(request, template, context)
