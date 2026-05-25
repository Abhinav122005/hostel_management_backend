from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.register_user, name="register_user"),
    path("login/", views.login_user, name="login_user"),
    path("send-otp/", views.send_user_otp, name="send_user_otp"),
    path("verify-otp/", views.verify_user_otp, name="verify_user_otp"),
    path("forgot-password/", views.forgot_user_password, name="forgot_user_password"),
    path("reset-password/", views.reset_user_password, name="reset_user_password"),
    path("<int:user_id>/", views.get_user_by_id, name="get_user_by_id"),
]
