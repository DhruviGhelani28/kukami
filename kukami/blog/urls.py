
from django.urls import path
from .models import *
from .views import *


urlpatterns = [
    path("posts/", PostListView.as_view(), name="post-list"),
    path("comments/", CommentListView.as_view(), name="comment-list"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    
    path("posts/create", PostCreateView.as_view(), name="post-create"),
    path("comments/create", CommentCreateView.as_view(), name="comment-create"),
    path("tags/create", TagCreateView.as_view(), name="tag-create"),
    
    path("posts/update/<str:pk>/", PostUpdateView.as_view(), name="post-update"),
    path("comments/update/<str:pk>/", CommentUpdateView.as_view(), name="comment-update"),
    path("tags/update/<str:pk>/", TagUpdateView.as_view(), name="tag-update"),
    
    path("posts/post/detail/<str:pk>/", PostDetailView.as_view(), name="post-detail"),
    
    
    path("posts/delete/<str:pk>/", PostDeleteView.as_view(), name="post-delete"),
    path("comments/delete/<str:pk>/", CommentDeleteView.as_view(), name="comment-delete"),
    path("tags/delete/<str:pk>/", TagDeleteView.as_view(), name="tag-delete"),
    # path("post-list", , name="post-list"),
    # path("post-list", , name="post-list"),
]
