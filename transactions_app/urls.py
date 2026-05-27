from django.urls import path
from . import views

urlpatterns = [
    path("initiate/", views.initiate_transaction, name="initiate_transaction"),
    path("verify/", views.verify_payu_payment, name="verify_payu_payment"),
    path("user/<int:user_id>/", views.get_user_transactions, name="get_user_transactions"),
    path("owner/<int:owner_id>/", views.get_owner_transactions, name="get_owner_transactions"),
]
