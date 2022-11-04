
from django.urls import path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home , name="home"),
    path('register/', views.register,name="register"),
    path('login/', views.login,name="login"),
    path('terms/', views.terms,name="terms"),
    path('policy/', views.policy,name="policy"),
    path('about/', views.about,name="about"),
    path('blogs/', views.blogs,name="blogs"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
