import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library
from ..connection import Connection

  
@login_required
def book_form(request):
    if request.method == 'GET':
        libraries = Library.objects.all()
        template = 'books/form.html'
        context = {
            'all_libraries': libraries
        }

        return render(request, template, context)

@login_required
def book_edit_form(request, book_id):

    if request.method == 'GET':
        book = Book.objects.get(pk=book_id)
        libraries = Library.objects.all()

        template = 'books/form.html'
        context = {
            'book': book,
            'all_libraries': libraries
        }

        return render(request, template, context)