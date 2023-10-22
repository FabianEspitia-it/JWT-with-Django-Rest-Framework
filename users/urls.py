from django.urls import path

from users.api.views import UsersRegisterAPIView, UsersLoginAPIView, UsersAPIView, UsersLogoutAPIView

urlpatterns = [
    path('register/', UsersRegisterAPIView.as_view(), name = "register"),
    path('login/', UsersLoginAPIView.as_view(), name = "login"),
    path('users/', UsersAPIView.as_view(), name = "users"),
    path('logout/', UsersLogoutAPIView.as_view(), name = "logout")


]
