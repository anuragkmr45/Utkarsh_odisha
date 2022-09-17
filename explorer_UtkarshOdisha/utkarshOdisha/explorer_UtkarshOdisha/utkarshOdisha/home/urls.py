from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="index"),
    path('login',views.loginUser, name="login"),
    path('logout',views.logoutUser, name="logout"),
    path("historical", views.historical, name="historical"),
    path("religious", views.religious, name="religious"),
    # path("historical", views.historical, name="historical"),
    # path("page3", views.page3, name="page3")
]
