from django.shortcuts import render, redirect
from .models import Book, Author, BookInstance, Genre, Comment
from django.views import generic
from .forms import CommentForm, RegisterUserForm, AuthUserForm
from django.contrib.auth import authenticate, login, logout
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

def log_out(request):
    logout(request)
    return redirect('/')    
    
    
def register_view(request):
    if request.method == 'POST':
        user_form = RegisterUserForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'catalog/register_done.html', {'new_user': new_user})
    else:
        user_form = RegisterUserForm()
    return render(request, 'catalog/registration.html', {'user_form': user_form})
    
    
    
    
    
    
    # next = request.GET.get('next')
    # form = RegisterUserForm(request.POST or None)
    # if form.is_valid():
        # user = form.save(commit=False)
        # password = form.cleaned_data.get('password')
        # user.set_password(password)
        # user.save()
        # new_user = authenticate(username = user.username, password = password)
        # login(request,user)
        # if next:
            # return redirect(next)
        # return redirect('/')
    # context = {
    # 'form': form,
                # }
    # return render(request, "catalog/registration.html", context)
    
    
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

class RegisterView(generic.View):
    
    def get(self, request, *args, **kwargs):
        form = AuthUserForm(request.POST or None)
        context = {'form': form}
        return render(request, 'catalog/login.html', context)

    def post(self, request, *args, **kwargs):
        form = AuthUserForm(request.POST or None)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        return render(request, 'catalog/login.html', {'form': form})
        
        
    
    

class RegistrationView(generic.CreateView):
    model = User
    template_name = 'catalog/registration.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('base')
    success_msg = 'User created. Congrat!!!'
    
    
