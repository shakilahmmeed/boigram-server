from django.urls import path
from account import views


urlpatterns = [
    path('login', views.CustomAuthToken.as_view()),
    path('register', views.RegisterView.as_view()),
    path('user', views.UserView.as_view()),
]
