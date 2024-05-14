from ..models import FixedRate
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic import DetailView

from Services.fixed_rate_services import FixedRateServices
from django.views.generic.edit import FormView

from ..forms import FixedRateForm
from django.urls import reverse_lazy


class CreateFixedRateView(LoginRequiredMixin, FormView):
    template_name = "investments/fixed_rate_form.html"
    form_class = FixedRateForm

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
        FixedRateServices.create_fixed_rate(form.cleaned_data)
        return super().form_valid(form)


class UpdateFixedRateView(LoginRequiredMixin, FormView):
    model = FixedRate
    form_class = FixedRateForm
    template_name = "investments/fixed_rate_form.html"

    def get_success_url(self):
        return reverse_lazy(
            # colocar para retornar no fixed_rate_detail
            "account:transactions_list",
            kwargs={"account_id": self.kwargs.get("account_id")},
        )

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["account_id"] = self.kwargs.get("account_id")
        kwargs["user_id"] = self.request.user.pk
        if self.kwargs.get("pk"):
            kwargs["instance"] = FixedRate.objects.get(pk=self.kwargs.get("pk"))
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
        fixed_rate_id = self.kwargs["pk"]
        FixedRateServices.update_fixed_rate(form.cleaned_data, fixed_rate_id)
        return super().form_valid(form)


class AccountDetailView(LoginRequiredMixin, DetailView):
    model = FixedRate
    template_name = "investments/fixed_rate_details.html"
    context_object_name = "fixed_rate"
