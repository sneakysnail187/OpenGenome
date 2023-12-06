from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about.html", views.about, name = "about"),
    path("postpage.html", views.postpage, name = "postpage"),
    path("upload.html", views.upload, name = "upload"),
    path("results.html", views.results, name = "results")
]