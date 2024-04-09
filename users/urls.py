from django.urls import path

from .views import (
    SignUpView,
    CategoriesListView,
    CreateCategoryView,
    DeleteCategoryView,
    CategoryUpdateView,
    FinancingsListView,
    CreateFinancingView,
)

app_name = "users"
urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("categories/", CategoriesListView.as_view(), name="categories_list"),
    path("categories/create/", CreateCategoryView.as_view(), name="create_category"),
    path(
        "categories/delete/<int:pk>/",
        DeleteCategoryView.as_view(),
        name="delete_category",
    ),
    path(
        "categories/update/<int:pk>/",
        CategoryUpdateView.as_view(),
        name="update_category",
    ),
    path("financings/", FinancingsListView.as_view(), name="financings_list"),
    path("financings/create/", CreateFinancingView.as_view(), name="create_financing"),
]
