from users.models import Financing


class FinancingServices:
    @staticmethod
    def fetch_financings_for_user(user):
        financings = Financing.objects.filter(user=user)
        return financings

    @staticmethod
    def create_financing(user, params):
        financing = Financing.objects.create(
            name=params["name"],
            parcels=params["parcels"],
            borrowed_value_cents=FinancingServices.convert_to_cents(
                params["borrowed_value_cents"]
            ),
            user_id=user.id,
        )
        return financing

    @staticmethod
    def convert_to_cents(value):
        return int(value * 100)

    @staticmethod
    def update_financing(user, params, financing_id):
        financing = Financing.objects.get(id=financing_id, user_id=user.id)
        financing.name = params["name"]
        financing.parcels = params["parcels"]
        financing.borrowed_value_cents = FinancingServices.convert_to_cents(
            params["borrowed_value_cents"]
        )
        financing.save()
        return financing
