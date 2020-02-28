from django.shortcuts import render,redirect
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from books.models import Book, Publisher, Author
from django.contrib import messages
# import operator
# from django.utils.six.moves import reduce

def homepage(request):
    return render(request, 'books/main.html')

def Book_list(request):
    books = Book.objects.all()
    print(books)
    return render(request, 'books/book_list.html', {'books':books})

def Publisher_list(request):
    publishers = Publisher.objects.all()
    print(publishers)
    return render(request, 'books/publisher_list.html', {'publishers':publishers})

def Author_list(request):
    authors = Author.objects.all()
    print(authors)
    return render(request, 'books/author_list.html', {'authors':authors})

def search_books (request):
    # a = Book.written.objects.all()
    try:
        keyword_b = request.POST['name']
        keyword_y = request.POST['year']
        namekeword = Book.objects.filter(title__startswith = keyword_b.lower(),published_date__year = keyword_y)
    except:
        namekeword = Book.objects.filter(title__startswith = keyword_b.lower())
        context = {'lstname':namekeword}
        return  render(request,'books/book_list.html',context)
    else:
        context = {'lstname':namekeword}
        return  render(request,'books/book_list.html',context)

    # filters = []
    # filters.append(models.Q(
    #     written__author_name=author_name,
    # ))
    # queryset = Book.objects.filter(reduce(operator.iand, filters))

def search_publisher (request):
    keyword_p = request.POST['name']
    namekeword = Publisher.objects.filter(name__startswith = keyword_p.capitalize())
    context = {'name':namekeword}
    print(namekeword)
    return  render(request,'books/publisher_list.html',context)

def search_author (request):
    keyword_a = request.POST['name']
    namekeword = Author.objects.filter(author_name__startswith = keyword_a.capitalize())
    context = {'name':namekeword}
    print(namekeword)
    return  render(request,'books/author_list.html',context)

def show_book(request):
    all_books = Book.objects.order_by('id')
    authors = Author.objects.all()
    publishers = Publisher.objects.all()
    context = {
        'all_books' : all_books,
        'authors' : authors,
        'publishers' : publishers
    }
    return render(request, 'home.html', context)