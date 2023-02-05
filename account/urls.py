from django.urls import path, include
from account.views import *

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name = 'register'),
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('profile/', UserProfileView.as_view(), name = 'profile'),
    # path('logout/', UserLogoutView.as_view(), name = 'logout'),
    path('changepassword/', UserChangePasswordView.as_view(), name = 'changepassword'),
    path('password_reset/', SendPasswordResetEmailView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uid>/<token>/', UserPasswordResetView.as_view(), name='password_reset_confirm'),
]
