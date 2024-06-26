from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from ..forms import CategoryForm, FinancingForm
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from Services.category_services import CategoryServices
from ..models import Category, Financing


class CategoriesListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = "users/categories/categories_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        fetch_categories_service = CategoryServices()
        return fetch_categories_service.fetch_categories_for_user(self.request.user)


class CreateCategoryView(LoginRequiredMixin, FormView):
    template_name = "users/categories/category_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("users:categories_list")

    def form_valid(self, form):
        CategoryServices.create_category(self.request.user, form.cleaned_data)
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, FormView):
    model = Category
    form_class = CategoryForm
    template_name = "users/category/categories_form.html"
    success_url = reverse_lazy("users:categories_list")

    def form_valid(self, form):
        category_id = self.kwargs["pk"]
        CategoryServices.update_category(
            self.request.user, form.cleaned_data, category_id
        )
        return super().form_valid(form)


class DeleteCategoryView(LoginRequiredMixin, DeleteView):
    model = Category
    success_url = reverse_lazy("users:categories_list")
