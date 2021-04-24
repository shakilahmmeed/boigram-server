from django.urls import path
from core import views


urlpatterns = [
    path('books', views.BookView.as_view()),
    path('book/<slug:book_slug>/', views.SingleBookView.as_view()),
    path('categories', views.CategoryView.as_view()),
    path('search', views.SearchView.as_view()),
]
