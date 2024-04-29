from django.urls import path

from .views import account_views

app_name = "account"
urlpatterns = [
    path("accounts/", account_views.AccountListView.as_view(), name="accounts_list"),
    path(
        "accounts/create/",
        account_views.CreateAccountView.as_view(),
        name="create_account",
    ),
    path(
        "accounts/<int:pk>/",
        account_views.AccountDetailView.as_view(),
        name="account_detail",
    ),
    path(
        "accounts/update/<int:pk>/",
        account_views.UpdateAccountView.as_view(),
        name="update_account",
    ),
    path(
        "accounts/delete/<int:pk>/",
        account_views.DeleteAccountView.as_view(),
        name="delete_account",
    ),
]
