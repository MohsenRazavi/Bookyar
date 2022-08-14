from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('blog/', include('blog.urls')),
    path('books/', include('books.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    
]