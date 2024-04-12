from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import FormView
from ..forms import InstallmentForm
from django.urls import reverse_lazy
from ..models import Installment
from Services.financing_services import FinancingServices


class ListInstallmentsView(LoginRequiredMixin, ListView):
    model = Installment
    template_name = "users/installments/installments_list.html"
    context_object_name = "installments"

    def get_queryset(self):
        financing_id = self.kwargs["financing_id"]
        return FinancingServices.fetch_installments_for_financing(
            user=self.request.user, financing_id=financing_id
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["financing_id"] = self.kwargs["financing_id"]
        return context


class CreateInstallmentView(LoginRequiredMixin, FormView):
    template_name = "users/installments/installment_form.html"
    form_class = InstallmentForm
    success_url = reverse_lazy("users:installments_list")

    def form_valid(self, form):
        financing_id = self.kwargs["financing_id"]
        FinancingServices.create_installment(
            self.request.user, form.cleaned_data, financing_id
        )
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["financing_id"] = self.kwargs["financing_id"]
        return context

    def get_success_url(self):
        financing_id = self.kwargs["financing_id"]
        return reverse_lazy(
            "users:installments_list", kwargs={"financing_id": financing_id}
        )
