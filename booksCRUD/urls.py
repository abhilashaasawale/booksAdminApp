from django.urls import path
from .views import SignUpView
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("admin_login/", views.admin_login, name="admin_login"),
    path("options/", views.options, name="options"),
    path("create/", views.create, name="create"),
    path("retrieve/", views.retrieve, name="retrieve"),
    path("update/", views.update, name="update"),
    path("delete/", views.delete, name="delete"),
    path("logout/", views.Logout, name="logout"),
]