from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Category, Financing
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from Services.category_services import CategoryServices
from Services.financing_services import FinancingServices

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, FinancingForm
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@method_decorator(login_required, name="dispatch")
class CategoriesListView(ListView):
    model = Category
    template_name = "users/categories_list.html"
    context_object_name = "categories"

    def get_queryset(self):
        fetch_categories_service = CategoryServices()
        return fetch_categories_service.fetch_categories_for_user(self.request.user)


class CreateCategoryView(LoginRequiredMixin, FormView):
    template_name = "users/category_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("users:categories_list")

    def form_valid(self, form):
        CategoryServices.create_category(self.request.user, form.cleaned_data)
        return super().form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, FormView):
    model = Category
    form_class = CategoryForm
    template_name = "users/category_form.html"
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


@method_decorator(login_required, name="dispatch")
class FinancingsListView(ListView):
    model = Financing
    template_name = "users/financings_list.html"
    context_object_name = "financings"

    def get_queryset(self):
        return FinancingServices.fetch_financings_for_user(user=self.request.user)


class CreateFinancingView(LoginRequiredMixin, FormView):
    template_name = "users/financing_form.html"
    form_class = FinancingForm
    success_url = reverse_lazy("users:financings_list")

    def form_valid(self, form):
        FinancingServices.create_financing(self.request.user, form.cleaned_data)
        return super().form_valid(form)


class DeleteFinancingView(LoginRequiredMixin, DeleteView):
    model = Financing
    # template_name = "users/financing_confirm_delete.html"
    success_url = reverse_lazy("users:financings_list")


class UpdateFinancingView(LoginRequiredMixin, FormView):
    model = Financing
    form_class = FinancingForm
    template_name = "users/financing_form.html"
    success_url = reverse_lazy("users:financings_list")

    def form_valid(self, form):
        financing_id = self.kwargs["pk"]
        FinancingServices.update_financing(
            self.request.user, form.cleaned_data, financing_id
        )
        return super().form_valid(form)


class ShowFinancingView(LoginRequiredMixin, DetailView):
    model = Financing
    template_name = "users/financing_detail.html"
