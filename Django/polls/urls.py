from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name = "about"),
    path("postpage/", views.postpage, name = "postpage"),
    path("analysis/", views.analysis, name = "analysis")
]