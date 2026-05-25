from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.register_owner, name="register_owner"),
    path("login/", views.login_owner, name="login_owner"),
    path("send-otp/", views.send_owner_otp, name="send_owner_otp"),
    path("verify-otp/", views.verify_owner_otp, name="verify_owner_otp"),
    path("forgot-password/", views.forgot_owner_password, name="forgot_owner_password"),
    path("reset-password/", views.reset_owner_password, name="reset_owner_password"),
    path("verify/<int:owner_id>/", views.verify_payu, name="verify_payu"),
]
