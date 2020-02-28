from django.contrib import admin
from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='books'
urlpatterns = [
       path('', views.homepage, name='homepage'),
       path('book/', views.Book_list, name='book_list'),
       path('pub/', views.Publisher_list, name='publisher_list'),
       path('au/', views.Author_list, name='author_list'),
       path('search/', views.search_books, name='search'),
       path('search_p/',views.search_publisher, name='search_p'),
       path('search_a/', views.search_author, name='search_a'),
       # path('login/', auth_views.LoginView.as_view() ,name='login'),
       # path('logout/', auth_views.LogoutView.as_view() ,name='logout')
       # path('ex_insert/', views.ex_insert, name='ex_insert'),
]
