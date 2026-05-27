from django.urls import path

from . import views


urlpatterns = [
    path("send/", views.send_request, name="send_request"),
    path("user/<int:user_id>/", views.get_user_requests, name="get_user_requests"),
    path("owner/<int:owner_id>/", views.get_owner_requests, name="get_owner_requests"),
    path("<int:request_id>/status/", views.update_request_status, name="update_request_status"),
    path("searchusers/", views.search_users, name="search_users"),
    path("hostel/<int:user_id>/", views.get_joined_hostel, name="get_joined_hostel"),
]
