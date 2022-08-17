from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<int:pk>/panel_info/', views.UserUpdateView.as_view(), name='panel'),
    path('<int:pk>/panel_needed_books/', views.user_needed_books_view, name='panel_needed_books'),
    path('<int:pk>/panel_added_books/', views.user_added_books_view, name='panel_added_books'),
    path('<int:pk>/panel_posts/', views.user_posts_view, name='panel_posts'),
]
