from django.shortcuts import render, redirect
from .models import Book, Author, BookInstance, Genre, Comment
from django.views import generic
from .forms import CommentForm, AuthUserForm, RegisterUserForm
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User

def index(request):
    comments = Comment.objects.order_by('-id')
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'catalog/base.html', {'comments': comments, 'num_visits': num_visits}, )

def create(request):
    error = ''
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('create_com')
        else:
            error = 'Wrong form!'


    form = CommentForm()
    context = {
        'form': form,
        'error': error
    }
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

class RegisterView(LoginView):
    template_name = 'catalog/login.html'
    form_class = AuthUserForm
    success_url = reverse_lazy('base')

class RegistrationView(generic.CreateView):
    model = User
    template_name = 'catalog/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('base')
    success_msg = 'User created. Congrat!!!'