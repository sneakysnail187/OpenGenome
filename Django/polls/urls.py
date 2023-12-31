from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("index.html", views.index, name= 'index'),
    path("about.html", views.about, name = "about"),
    path("postpage.html", views.postpage, name = "postpage"),
    path("upload.html", views.upload, name = "upload"),
    path("results.html", views.results, name = "results"),
    path("analytics.html", views.analytics, name = "analytics"),
    path("forum.html", views.forum, name ="forum"),

]