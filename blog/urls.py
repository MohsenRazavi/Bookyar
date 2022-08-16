from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogPostList.as_view(), name='blog_list'),
    path('<int:pk>/', views.blog_post_detail_view, name='blog_detail'),
    path('<int:pk>/update', views.BlogPostUpdate.as_view(), name='blog_update'),
    path('<int:pk>/post-delete', views.BlogPostDelete.as_view(), name='blog_delete'),
    path('<int:pk>/comment-delete', views.BlogCommentDelete.as_view(), name='comment_delete'),
    path('create/', views.blog_post_create, name='blog_create'),

]