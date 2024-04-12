from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from ..forms import FinancingForm
from Services.financing_services import FinancingServices
from django.views.generic import CreateView, ListView, DeleteView, DetailView
from ..models import Financing
from django.urls import reverse_lazy


class FinancingsListView(LoginRequiredMixin, ListView):
    model = Financing
    template_name = "users/financings/financings_list.html"
    context_object_name = "financings"

    def get_queryset(self):
        return FinancingServices.fetch_financings_for_user(user=self.request.user)


class CreateFinancingView(LoginRequiredMixin, FormView):
    template_name = "users/financing/financings_form.html"
    form_class = FinancingForm
    success_url = reverse_lazy("users:financings_list")

    def form_valid(self, form):
        FinancingServices.create_financing(self.request.user, form.cleaned_data)
        return super().form_valid(form)


class DeleteFinancingView(LoginRequiredMixin, DeleteView):
    model = Financing
    success_url = reverse_lazy("users:financings_list")


class UpdateFinancingView(LoginRequiredMixin, FormView):
    model = Financing
    form_class = FinancingForm
    template_name = "users/financing/financings_form.html"
    success_url = reverse_lazy("users:financings_list")

    def form_valid(self, form):
        financing_id = self.kwargs["pk"]
        FinancingServices.update_financing(
            self.request.user, form.cleaned_data, financing_id
        )
        return super().form_valid(form)


class ShowFinancingView(LoginRequiredMixin, DetailView):
    model = Financing
    template_name = "users/financings/financing_detail.html"
