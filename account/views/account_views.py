from ..models import Account
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView
from Services.account_services import AccountServices
from django.views.generic.edit import FormView
from ..forms import AccountForm
from django.urls import reverse_lazy
from django.core import serializers


class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    template_name = "accounts/account_list.html"
    context_object_name = "accounts"

    def get_queryset(self):
        return AccountServices.fetch_accounts_for_user(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accounts_json"] = serializers.serialize("json", self.get_queryset())
        return context


class CreateAccountView(LoginRequiredMixin, FormView):
    template_name = "accounts/account_form.html"
    form_class = AccountForm
    success_url = reverse_lazy("account:accounts_list")

    def form_valid(self, form):
        AccountServices.create_account(self.request.user, form.cleaned_data)
        return super().form_valid(form)


class AccountDetailView(LoginRequiredMixin, DetailView):
    model = Account
    template_name = "accounts/account_detail.html"
    context_object_name = "account"


class UpdateAccountView(LoginRequiredMixin, FormView):
    model = Account
    form_class = AccountForm
    template_name = "accounts/account_form.html"
    success_url = reverse_lazy("account:accounts_list")

    def form_valid(self, form):
        account_id = self.kwargs["pk"]
        AccountServices.update_account(self.request.user, form.cleaned_data, account_id)
        return super().form_valid(form)


class DeleteAccountView(LoginRequiredMixin, DeleteView):
    model = Account
    success_url = reverse_lazy("account:accounts_list")
    context_object_name = "account"
