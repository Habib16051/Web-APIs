from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
# Create your views here.


class ListBook(ListView):
    model = Book
    template_name = 'list_book.html'
