from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.Login, name="login"),
    path("register/", views.register, name="register"),
    path("addItem/",views.register, name = "addItem"),
    path("history/",views.register,name = "history")
    #path("logout/", views.Logout, name="logout"),
]