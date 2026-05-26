from django.urls import path

from . import views


urlpatterns = [
    path("add/", views.create_booking, name="create_booking"),
    path("user/<int:user_id>/", views.get_user_bookings, name="get_user_bookings"),
    path("all/", views.get_all_bookings, name="get_all_bookings"),
    path("<int:booking_id>/status/", views.update_booking_status, name="update_booking_status"),
    path("<int:booking_id>/approve/", views.approve_booking, name="approve_booking"),
    path("<int:booking_id>/reject/", views.reject_booking, name="reject_booking"),
]
