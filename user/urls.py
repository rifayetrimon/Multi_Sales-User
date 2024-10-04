from django.urls import path
from . views import login_view, home_view, logout_view, otp_verify_view, profile_update_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('otp_verify/', otp_verify_view, name='otp_verify'),
    path('profile_update/', profile_update_view, name='profile_update'),

    path('pssword_reset/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
    ), name='password_reset'),

    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html',
    ), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
    ), name='password_reset_confirm'),

    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html',
    ), name='password_reset_complete'),
]