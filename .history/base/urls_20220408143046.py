from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.CustomLogin.as_view(), name="login")
    path("", views.t)
]
