from django.shortcuts import render, redirect
from .const import *


def index(request):
    context = {'title': 'Главная'}
    return render(request, 'writers_app/index.html', context)


def writers(request):
    writers = request.GET.get('writers')
    year = request.GET.get('year')
    if writers and year and writers in WRITERS_INFO:
        books = {}
        for book in AUTHOR_BOOKS[writers]:
            if (book in BOOKS) and (BOOKS[book]['year'] == int(year)):
                books[book] = BOOKS[book]
        context = {
            'title': 'URL поиск',
            'writer_name': writers,
            'books': books,
        }
        return render(request, 'writers_app/writers/url_books.html', context)
    context = {'title': 'Писатели'}
    return render(request, 'writers_app/writers.html', context)


def best_books(request):
    context = {
        'title': 'Топ книг',
        'top_books': dict(sorted(BOOKS.items(), key=lambda item: item[1]['position'])),
    }
    return render(request, 'writers_app/best_books.html', context)


def writers_name(request, writer_name):
    if writer_name in WRITERS_INFO:
        books = {}
        for book in AUTHOR_BOOKS[writer_name]:
            if book in BOOKS:
                books[book] = BOOKS[book]
        context = {
            'title': f"Писатели | {WRITERS_INFO[writer_name]['name']}",
            'info_writers': WRITERS_INFO[writer_name],
            'writer_name': writer_name,
            'books': books,
        }
        return render(request, 'writers_app/writers/info_writers.html', context)
    return redirect('/writers/')


def book_info(request, writer_name, name_book):
    if name_book in BOOKS:
        context = {
            'title': f"{BOOKS[name_book]['author']} | {BOOKS[name_book]['title']}",
            'info_book': BOOKS[name_book],
        }
        return render(request, 'writers_app/writers/books.html', context)
    return redirect(f'/writers/{writer_name}/')


def best_book_info(request, number_book):
    sorted_books_top = dict(sorted(BOOKS.items(), key=lambda item: item[1]['position']))
    books_keys = list(sorted_books_top.keys())
    if number_book <= len(books_keys) and number_book > 0:
        context = {
            'title': 'Топ книг',
            'info_book': sorted_books_top[books_keys[number_book - 1]]
        }
        return render(request, 'writers_app/writers/books.html', context)
    return redirect('/best_books/')
