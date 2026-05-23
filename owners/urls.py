from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.register_owner, name="register_owner"),
    path("login/", views.login_owner, name="login_owner"),
    path("verify/<int:owner_id>/", views.verify_payu, name="verify_payu"),
]
