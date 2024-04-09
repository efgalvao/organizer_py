from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .models import Category
from django.views.generic import CreateView, ListView, DeleteView
from Services.category_services import CategoryServices
from django.shortcuts import render

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm
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
    template_name = 'categories/category_form.html'

    def form_valid(self, form):
        category_id = self.kwargs['pk']
        CategoryServices.update_category(
            self.request.user, form.cleaned_data, category_id)
        return super().form_valid(form)


class DeleteCategoryView(LoginRequiredMixin, DeleteView):
    model = Category
    template_name = "users/category_confirm_delete.html"
    success_url = reverse_lazy("users:categories_list")
