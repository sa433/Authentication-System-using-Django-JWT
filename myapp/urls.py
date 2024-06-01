from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('changepw/', views.UserChangePassword.as_view(), name='changepw'),
    path('send-reset-password/', views.SendResetPasswordView.as_view(), name='send-reset-pw'),
    path('reset-password/<uid>/<token>/', views.UserPasswordResetView.as_view(), name='')
]