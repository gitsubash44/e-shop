from django.urls import path
from app import views

urlpatterns = [
    path('',views.index,name="index"),
    path('blog/',views.blog,name="blog"),
]