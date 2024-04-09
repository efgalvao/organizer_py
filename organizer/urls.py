from django.urls import path

from .views import (
    AccountListView,
    CreateAccountView,
    AccountDetailView,
    UpdateAccountView,
    DeleteAccountView,
)

app_name = "organizer"
urlpatterns = [
    path("accounts/", AccountListView.as_view(), name="accounts_list"),
    path("accounts/create/", CreateAccountView.as_view(), name="create_account"),
    path("accounts/<int:pk>/", AccountDetailView.as_view(), name="account_detail"),
    path(
        "accounts/update/<int:pk>/", UpdateAccountView.as_view(), name="update_account"
    ),
    path(
        "accounts/delete/<int:pk>/", DeleteAccountView.as_view(), name="delete_account"
    ),
]
