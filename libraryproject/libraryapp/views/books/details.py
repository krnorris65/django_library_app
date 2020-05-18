import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library, Librarian
# from libraryapp.models import model_factory
from ..connection import Connection

def create_book(cursor, row):
    _row = sqlite3.Row(cursor, row)

    book = Book()
    book.id = _row["book_id"]
    book.author = _row["author"]
    book.isbn = _row["isbn"]
    book.title = _row["title"]
    book.year_published = _row["year_published"]

    librarian = Librarian()
    librarian.id = _row["librarian_id"]
    librarian.first_name = _row["first_name"]
    librarian.last_name = _row["last_name"]

    library = Library()
    library.id = _row["library_id"]
    library.title = _row["library_name"]

    book.librarian = librarian
    book.location = library

    return book


@login_required
def book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'GET':

        template = 'books/detail.html'
        context = {
            'book': book
        }

        return render(request, template, context)
    if request.method == 'POST':
        form_data = request.POST
        # Check if this POST is for editing a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):

            book.title = form_data['title'] 
            book.author = form_data['author'] 
            book.isbn = form_data['isbn']
            book.year_published = form_data['year_published'] 
            book.location_id = form_data["location"]
        
            book.save()

            return redirect(reverse('libraryapp:books'))

        # Check if this POST is for deleting a book
        #
        # Note: You can use parenthesis to break up complex
        #       `if` statements for higher readability
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            book.delete()

            return redirect(reverse('libraryapp:books'))