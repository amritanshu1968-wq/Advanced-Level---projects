
from django.urls import path
from . import views
urlpatterns=[
 path('', views.home, name='home'),
 path('login/', views.login_view, name='login'),
 path('register/', views.register, name='register'),
 path('logout/', views.logout_view, name='logout'),
 path('create/', views.create_post, name='create_post'),
 path('post/<int:pk>/', views.post_detail, name='post_detail'),
 path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
]
