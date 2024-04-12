from django.urls import path

from .views import (
    auth_views,
    category_views,
    financing_views,
    installment_views,
)

app_name = "users"
urlpatterns = [
    path("signup/", auth_views.SignUpView.as_view(), name="signup"),
    path(
        "categories/",
        category_views.CategoriesListView.as_view(),
        name="categories_list",
    ),
    path(
        "categories/create/",
        category_views.CreateCategoryView.as_view(),
        name="create_category",
    ),
    path(
        "categories/delete/<int:pk>/",
        category_views.DeleteCategoryView.as_view(),
        name="delete_category",
    ),
    path(
        "categories/update/<int:pk>/",
        category_views.CategoryUpdateView.as_view(),
        name="update_category",
    ),
    path(
        "financings/",
        financing_views.FinancingsListView.as_view(),
        name="financings_list",
    ),
    path(
        "financings/create/",
        financing_views.CreateFinancingView.as_view(),
        name="create_financing",
    ),
    path(
        "financings/delete/<int:pk>/",
        financing_views.DeleteFinancingView.as_view(),
        name="delete_financing",
    ),
    path(
        "financings/update/<int:pk>/",
        financing_views.UpdateFinancingView.as_view(),
        name="update_financing",
    ),
    path(
        "financings/show/<int:pk>/",
        financing_views.ShowFinancingView.as_view(),
        name="show_financing",
    ),
    path(
        "financings/<int:financing_id>/installments/",
        installment_views.ListInstallmentsView.as_view(),
        name="installments_list",
    ),
    path(
        "financings/<int:financing_id>/installments/create/",
        installment_views.CreateInstallmentView.as_view(),
        name="create_installment",
    ),
]
