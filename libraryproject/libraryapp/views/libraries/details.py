import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Library
from libraryapp.models import model_factory
from ..connection import Connection


@login_required
def library_details(request, library_id):
    if request.method == 'GET':
        library = Library.objects.get(pk=library_id)

        template = 'libraries/detail.html'
        context = {
            'library': library
        }

        return render(request, template, context)