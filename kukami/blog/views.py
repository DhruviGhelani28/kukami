from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import *
from django.urls import reverse_lazy
from .forms import PostCreateForm, CommentCreateForm, TagCreateForm

from django.shortcuts import get_object_or_404
# Create your views here.

class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    template_name = "post_list.html"
    success_url = reverse_lazy("post-list")

class CommentListView(ListView):
    model = Comment
    queryset = Comment.objects.all()
    template_name = "comment_list.html"
    success_url = reverse_lazy("comment-list")
    
class TagListView(ListView):
    model = Tag
    queryset = Tag.objects.all()
    template_name = "tag_list.html"
    success_url = reverse_lazy("tag-list")
    

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = "create_post.html"
    success_url = reverse_lazy("post-list")
    
class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = "create_post.html"
    success_url = reverse_lazy("comment-list")
    
class TagCreateView(CreateView):
    model = Tag
    form_class = TagCreateForm
    template_name = "create_post.html"
    success_url = reverse_lazy("tag-list")
    
    
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostCreateForm
    template_name = "create_post.html"
    success_url = reverse_lazy("post-list")

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = "create_post.html"
    success_url = reverse_lazy("comment-list")    

class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagCreateForm
    template_name = "create_post.html"
    success_url = reverse_lazy("tag-list")
    
class PostDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        obj = get_object_or_404(Post, pk = kwargs.get('pk'))
        print(obj)
        print(self.get_object())
        context['comments'] = obj.post_comment.all()
        context['tags'] = obj.tags.all()
        return context
    
    
class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_confirm_delete.html"
    success_url = reverse_lazy("post-list")
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        obj = get_object_or_404(Post, pk = kwargs['pk'])
        obj.tags.clear()
        obj.post_comment.all().delete()
        return super().post(request, *args, **kwargs)

class CommentDeleteView(DeleteView):
    model = Comment
    success_url = reverse_lazy("comment-list")    

class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tag-list")