from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:pk>", views.entries, name="detail"),
    path("create/", views.create, name="create"),
    path("duplicate/", views.duplicate, name="duplicate"),
    path("edit/<str:pk>", views.edit, name="edit"),
    path("delete/<str:pk>", views.delete, name="delete"),
    path("search/", views.search, name="search"),
    path("404/", views.notfound, name="notfound")
]
