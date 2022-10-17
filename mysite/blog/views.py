from django.shortcuts import render
from django.urls import is_valid_path

from blog import views

urlpatterns = [
    path("", views.PostView.as_view(), name="home"),
    path("<slug:slug>/", views.PostDetail.as_view(), name="post_detail"),
]
# Create your views here.
