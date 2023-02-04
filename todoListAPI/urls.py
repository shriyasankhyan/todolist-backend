
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('todo_api.urls')),
    path('api/user/', include('account.urls')),
]
