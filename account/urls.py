from django.urls import path, include
from account.views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name = 'register'),
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('profile/', UserProfileView.as_view(), name = 'profile'),
    # path('logout/', UserLogoutView.as_view(), name = 'logout'),
    path('changepassword/', UserChangePasswordView.as_view(), name = 'changepassword'),
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('password-reset-confirm/<uid>/<token>/', UserPasswordResetView.as_view(), name='password-reset-confirm')
    # path('logout/', UserLogoutView.as_view(), name='logout')
]
