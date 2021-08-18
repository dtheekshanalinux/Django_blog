from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from register import views as v
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/", v.register, name="register"),
    path('', include('blog.urls')),
    path('register/', include("django.contrib.auth.urls")),
    path('/register', include('register.urls')),
    path("summernote/", include("django_summernote.urls")),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)