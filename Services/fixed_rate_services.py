from account.models import FixedRate


class FixedRateServices:
    @staticmethod
    def create_fixed_rate(params):
        fixed_rate = FixedRate.objects.create(
            account_id=params["account_id"],
            name=params["name"],
            invested_cents=FixedRateServices.convert_to_cents(params["invested_cents"]),
            current_balance_cents=FixedRateServices.convert_to_cents(
                params["current_balance_cents"]
            ),
            released=params["released"],
        )
        return fixed_rate

    @staticmethod
    def update_fixed_rate(params, fixed_rate_id):
        fixed_rate = FixedRate.objects.get(pk=fixed_rate_id)
        fixed_rate.name = params["name"]
        fixed_rate.invested_cents = FixedRateServices.convert_to_cents(
            params["invested_cents"]
        )
        fixed_rate.current_balance_cents = FixedRateServices.convert_to_cents(
            params["current_balance_cents"]
        )
        fixed_rate.released = params["released"]
        fixed_rate.save()
        return fixed_rate

    @staticmethod
    def convert_to_cents(value):
        return int(float(value) * 100)
