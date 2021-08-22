from . import views
from django.urls import path
from .views import AddPostView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('about-us.html', views.aboutus, name='about-us'),
    path('contact-us.html', views.contactus, name='contact-us'),
    path('add_post.html', AddPostView.as_view(), name='add_post'),
] 
