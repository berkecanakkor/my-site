from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="home"),
    path('index', views.index),
    path('blogs', views.blogs, name="blogs"),
    path('blogs/<slug:slug>', views.blog_details, name="blog_details"),
    path('category/<slug:slug>', views.blogs_by_category, name="blogs_by_category"),
    path('about', views.about, name="about"),
    path('become_advisor',views.become_advisor, name='become_advisor' )
]
