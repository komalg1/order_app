from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.Login, name="Login"),
    path("index/", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("addItem/",views.addItem, name = "addItem"),
    path("history/",views.history,name = "history"),
    path("logout/", views.Logout, name="logout"),
]