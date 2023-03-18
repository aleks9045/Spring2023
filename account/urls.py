from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='registration/login.html',
        next_page=None
    ), name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        template_name='registration/logout.html',
        next_page=None
    ), name='logout'),

    path('', views.dashboard, name='dashboard'),

    path('password_change/',
         auth_views.PasswordChangeView.as_view(
             template_name='registration/password_change_form_.html'
         ),
         name='password_change'),

    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(
            template_name='registration/password_change_done_.html',
         ), name='password_change_done'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(
            template_name='registration/password_reset_form_.html'
         ), name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
            template_name='registration/password_reset_done_.html'
         ), name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='registration/password_reset_confirm.html'
         ), name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete_.html'
         ), name='password_reset_complete'),

    path('register/', views.register, name='register')

]
