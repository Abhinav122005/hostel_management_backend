from django.urls import path

from . import views


urlpatterns = [
    path("all/", views.get_all_hostels, name="get_all_hostels"),
    path("top-rated/", views.get_top_rated_hostels, name="get_top_rated_hostels"),
    path("search/", views.get_hostels_by_area, name="get_hostels_by_area"),
    path("single/<int:hostel_id>/", views.get_single_hostel, name="get_single_hostel"),
    path("filter/", views.filter_by_type, name="filter_by_type"),
    path("search-combo/", views.search_by_area_and_type, name="search_by_area_and_type"),
    path("nearby/", views.get_nearby_hostels, name="get_nearby_hostels"),
    path("nearby/top-rated/", views.get_top_rated_hostels, name="get_nearby_top_rated_hostels"),
    path("add/", views.add_hostel, name="add_hostel"),
    path("book/<int:hostel_id>/", views.decrement_vacancy, name="decrement_vacancy"),
    path("user/joined/<int:user_id>/", views.get_user_joined_hostel, name="get_user_joined_hostel"),
    path("owner/<int:owner_id>/", views.get_hostels_by_owner, name="get_hostels_by_owner"),
    path("delete/<int:hostel_id>/", views.delete_hostel, name="delete_hostel"),
    path("owner/<int:owner_id>/hostel-users/", views.get_hostels_with_users, name="get_hostels_with_users"),
    path("<int:hostel_id>/", views.get_hostel_by_id, name="get_hostel_by_id"),
]
