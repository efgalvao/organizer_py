from models import FixedRate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from Services.investment_services import InvestmentServices

from django.urls import reverse_lazy


class InvestmentListView(LoginRequiredMixin, ListView):
    template_name = "investments/investment_list.html"
    context_object_name = "investments"

    def get_queryset(self):
        user = self.request.user
        account_id = self.kwargs.get("account_id", None)
        return InvestmentServices.fetch_investments_for_account(account_id, user.pk)

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data()
        context["account_id"] = self.kwargs.get("account_id", None)
        return self.render_to_response(context)
