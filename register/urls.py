from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from register import views as v
from django.contrib.auth import views

urlpatterns = [
    path("register/", v.register, name="register"),
    path('login/',views.LoginView.as_view(template_name="registration/login.html"),name='login'),
    path('logout/',views.LogoutView.as_view(template_name="registration/logout.html"),name='logout'),
]