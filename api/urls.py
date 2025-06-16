from django.urls import path
from .views import (
    PublicDataList,
    PrivateDataList,
    RegisterView,
    LoginView,
)

urlpatterns = [
    path('public/', PublicDataList.as_view(), name='public-data'),
    path('private/', PrivateDataList.as_view(), name='private-data'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]