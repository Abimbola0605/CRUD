from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .import urls
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

class PostListView(generic.ListView):
    model = Post

class PostCreateView(generic.CreateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDetailView(generic.DetailView):
    model = Post

class PostUpdateView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")

class PostDeleteView(generic.UpdateView):
    model = Post
    fields = "__all__"
    success_url = reverse_lazy("blog:all")
