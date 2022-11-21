from django.urls import path
from blogapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import MyPasswordResetForm ,MySetPasswordForm

urlpatterns = [
    path('', views.home , name="home"),
    path('all-blogs/', views.all_blogs,name="all-blogs"),
    path('add-blog/', views.add_blog,name="add-blog"),
    path('register/', views.register,name="register"),
    path('check_user_exist/', views.check_user_exist,name="check_user_exist"),
    path('check_email_exist/', views.check_email_exist,name="check_email_exist"),
    path('login/', views.user_login,name="login"),
    path('logout/', views.user_logout,name="logout"),
    path('terms/', views.terms,name="terms"),
    path('policy/', views.policy,name="policy"),
    path('about/', views.about,name="about"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='blogapp/reset_password.html',form_class=MyPasswordResetForm),name='reset_password'),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name='blogapp/reset_password_done.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='blogapp/reset_password_confirm.html',form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='blogapp/reset_password_complete.html'),name='password_reset_complete'),
    path('edit-profile/<username>', views.edit_profile,name="edit-profile"),
    path('profile/<username>/', views.profile,name="profile"),
    path('category/<slug:slug>/',views.category,name='category'),
    path('<slug:slug>/', views.detail,name="detail"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
