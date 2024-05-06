from django.urls import path

from .views import account_views
from .views import transaction_views

app_name = "account"
urlpatterns = [
    path("", account_views.AccountListView.as_view(), name="account_list"),
    path(
        "accounts/create/",
        account_views.CreateAccountView.as_view(),
        name="create_account",
    ),
    path(
        "accounts/<int:pk>/",
        account_views.AccountDetailView.as_view(),
        name="account_details",
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
    path(
        "<int:account_id>/transactions/",
        transaction_views.TransactionListView.as_view(),
        name="transactions_list",
    ),
    path(
        "<int:account_id>/transactions/create/",
        transaction_views.CreateTransactionView.as_view(),
        name="create_transaction",
    ),
    path(
        "<int:account_id>/transactions/update/<int:pk>/",
        transaction_views.UpdateTransactionView.as_view(),
        name="update_transaction",
    ),
]
