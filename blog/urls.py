from . import views
from django.urls import path
from .views import AddPostView, UpdatePostView, DeletePostView, CategoryView, LikeView

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('about-us.html', views.aboutus, name='about-us'),
    path('contact-us.html', views.contactus, name='contact-us'),
    path('add_post.html', AddPostView.as_view(), name='add_post'),
    path('edit/<slug:slug>/', UpdatePostView.as_view(), name='update_post'),
    path('<slug:slug>/delete', DeletePostView.as_view(), name='delete_post'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('like/<slug:slug>', LikeView, name="like_post")
] 
