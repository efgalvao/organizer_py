from ..models import Transaction
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView

from Services.transaction_services import TransactionServices
from django.views.generic.edit import FormView

from ..forms import TransactionForm
from django.urls import reverse_lazy
from django.core import serializers


class TransactionListView(LoginRequiredMixin, ListView):
    model = Transaction
    template_name = "transactions/transaction_list.html"
    context_object_name = "transactions"

    def get_queryset(self):
        user = self.request.user
        account_id = self.kwargs.get("account_id", None)
        return TransactionServices.fetch_transactions_for_account(account_id, user.pk)

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        context["account_id"] = self.kwargs.get("account_id", None)
        return self.render_to_response(context)


class CreateTransactionView(LoginRequiredMixin, FormView):
    template_name = "transactions/transaction_form.html"
    form_class = TransactionForm

    def get_success_url(self):
        return reverse_lazy(
            "account:transactions_list",
            kwargs={"account_id": self.kwargs.get("account_id")},
        )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["account_id"] = self.kwargs.get("account_id")
        kwargs["user_id"] = self.request.user.pk
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial["account_id"] = self.kwargs.get("account_id")
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["account_id"] = self.kwargs.get("account_id")
        return context

    def form_valid(self, form):
        TransactionServices.create_transaction(self.request.user, form.cleaned_data)
        return super().form_valid(form)


class UpdateTransactionView(LoginRequiredMixin, FormView):
    model = Transaction
    form_class = TransactionForm
    template_name = "transactions/transaction_form.html"

    def get_success_url(self):
        return reverse_lazy(
            "account:transactions_list",
            kwargs={"account_id": self.kwargs.get("account_id")},
        )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["account_id"] = self.kwargs.get("account_id")
        kwargs["user_id"] = self.request.user.pk
        if self.kwargs.get("pk"):
            kwargs["instance"] = Transaction.objects.get(pk=self.kwargs.get("pk"))
        return kwargs

    def get_initial(self):
        initial = super().get_initial()
        initial["account_id"] = self.kwargs.get("account_id")
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["account_id"] = self.kwargs.get("account_id")
        return context

    def form_valid(self, form):
        transaction_id = self.kwargs["pk"]
        TransactionServices.update_transaction(form.cleaned_data, transaction_id)
        return super().form_valid(form)
