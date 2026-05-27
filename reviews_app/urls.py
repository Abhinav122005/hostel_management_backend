from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_review, name="add_review"),
    path("hostel/<int:hostel_id>/", views.get_hostel_reviews, name="get_hostel_reviews"),
    path("<int:review_id>/delete/", views.delete_review, name="delete_review"),
]
