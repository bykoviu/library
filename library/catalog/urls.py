from django.urls import path
from . import views


urlpatterns = [
        path('', views.index),
        path('books', views.BookListView.as_view(), name='books'),
        path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
        path('authors', views.AuthorListView.as_view(), name='authors'),
        path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
        path('genres', views.GenreListView.as_view(), name='genres'),
        path('create_com', views.create, name='create_com'),
        path('login', views.RegisterView.as_view(), name='login'),
        path('Register', views.RegistrationView.as_view(), name='register'),

]