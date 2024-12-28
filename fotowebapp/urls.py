from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("galary/", views.galary, name="galary"),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("blog/", views.blog, name="blog"),
]