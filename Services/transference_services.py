from users.models import Transference
from datetime import date


class TransferenceServices:
    @staticmethod
    def fetch_transferences_for_user(user):
        today = date.today()
        first_day_of_month = today.replace(day=1)
        transferences = Transference.objects.filter(
            user=user, date__gte=first_day_of_month
        ).order_by("-date")
        return transferences

    @staticmethod
    def create_transference(user, params):
        transference = Transference.objects.create(
            user_id=user.id,
            receiver=params["receiver"],
            sender=params["sender"],
            value_cents=TransferenceServices.value_to_cents(params["value_cents"]),
            date=params["date"],
        )
        return transference

    @staticmethod
    def value_to_cents(value):
        return int(value * 100)
