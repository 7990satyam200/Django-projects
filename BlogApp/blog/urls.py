from django.urls import path
from . import views

urlpatterns=[
    path('', views.Blog.as_view(), name='home'),
    path('post/<int:pk>/', views.Detail.as_view(), name='post_detail'),

]
