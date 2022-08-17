from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('<int:pk>/panel_info/', views.UserUpdateView.as_view(), name='panel'),
]
