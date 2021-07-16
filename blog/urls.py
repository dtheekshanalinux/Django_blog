from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('about-us.html', views.aboutus, name='about-us'),
    path('contact-us.html', views.contactus, name='contact-us'),
] 
