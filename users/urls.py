from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("<int:user_id>/", views.get_user_by_id, name="get_user_by_id"),
]
