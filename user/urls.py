from django.urls import path
from . views import login_view, home_view, logout_view, otp_verify_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('logout/', logout_view, name='logout'),
    path('otp_verify/', otp_verify_view, name='otp_verify'),
]