import sqlite3
from django.shortcuts import render, redirect, reverse
from libraryapp.models import Library, Book
# from libraryapp.models import model_factory
from ..connection import Connection
from django.contrib.auth.decorators import login_required


@login_required
def library_list(request):
    if request.method == 'GET':
        all_books = Book.objects.all()
        all_libraries = Library.objects.all()

        for library in all_libraries:
            books = all_books.filter(location_id=library.id)
            library.books = books

        template_name = 'libraries/list.html'

        context = {
            'all_libraries': all_libraries
        }

        return render(request, template_name, context)
    elif request.method == 'POST':
        form_data = request.POST

        new_library = Library(
            title = form_data['title'], 
            address = form_data['address']
        )

        new_library.save()
                

        return redirect(reverse('libraryapp:libraries'))
