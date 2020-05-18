import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Librarian
from ..connection import Connection


@login_required
def librarian_details(request, librarian_id):
    if request.method == 'GET':
        librarian = Librarian.objects.get(pk=librarian_id)

        template = 'librarians/detail.html'
        context = {
            'librarian': librarian
        }

        return render(request, template, context)