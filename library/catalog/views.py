from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre, Comment
from django.views import generic
from .forms import CommentForm

def index(request):
    comments = Comment.objects.order_by('-id')
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'catalog/base.html', {'comments': comments, 'num_visits': num_visits}, )

def create(request):
    form = CommentForm()
    context = {'form': form}
    return render(request, 'catalog/create_com.html')

def boks_list(request):

    return render(request, 'catalog/book_list.html', )

def author_list(request):
    return render(request, 'catalog/author_list.html')

def genres(request):
    return render(request, 'catalog/genre_list.html')


class BookListView(generic.ListView):
    model = Book


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


class AuthorDetailView(generic.DetailView):
    model = Author


class GenreListView(generic.ListView):
    model = Genre