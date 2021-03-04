from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from series.variables import GENRE_CHOICES

app_name = "account"

urlpatterns = [

    # account/login/
    path('login/', views.user_login, name='user_login'),

    # account/logout/
    path('logout/', auth_views.LogoutView.as_view(template_name="account/logout.html"), name='user_logout'),

    # account/register/
    path('register/', views.register, name='user_register'),

    # /account/profile
    url(r'^profile/$', views.profile, name='profile'),

    path('password-change/', auth_views.PasswordChangeView.as_view(
                                    template_name="series/profile.html",
                                    success_url="/account/password-change-done/"),
         name='password_change'),

    path('password-change-done/', auth_views.PasswordChangeDoneView.as_view(
                                    template_name="account/password_change_done.html"),
         name='password_change_done'),

]
