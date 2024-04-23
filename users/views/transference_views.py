from ..models import Transference
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView
from ..forms import TransferenceForm
from django.urls import reverse_lazy
from Services.transference_services import TransferenceServices


class CreateTransferenceView(LoginRequiredMixin, CreateView):
    template_name = "users/transferences/transference_form.html"
    form_class = TransferenceForm
    success_url = reverse_lazy("users:transference_list")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"user": self.request.user})
        return kwargs

    def form_valid(self, form):
        TransferenceServices.create_transference(self.request.user, form.cleaned_data)
        return super().form_valid(form)


class TransferenceListView(LoginRequiredMixin, ListView):
    model = Transference
    template_name = "users/transferences/transference_list.html"
    context_object_name = "transferences"

    def get_queryset(self):
        return TransferenceServices.fetch_transferences_for_user(self.request.user)
