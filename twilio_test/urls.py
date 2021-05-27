from django.contrib import admin
from django.urls import path, include

from users.views import UserRegisterView, UserLoginView, CheckCodeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/register/', UserRegisterView.as_view()),
    path('user/login/', UserLoginView.as_view()),
    path('user/check/', CheckCodeView.as_view({'get': 'list', 'post': 'create'})),
]
