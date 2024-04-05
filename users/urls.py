from django.urls import path

from .views import (
    SignUpView,
    CategoriesListView,
    CreateCategoryView,
    DeleteCategoryView,
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
]
