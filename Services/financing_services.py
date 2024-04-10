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

    @staticmethod
    def fetch_installments_for_financing(user, financing_id):
        financing = Financing.objects.get(id=financing_id, user=user)
        installments = financing.installments.all().order_by("parcel")
        return installments

    @staticmethod
    def create_installment(user, params, financing_id):
        financing = Financing.objects.get(id=financing_id, user=user)
        installment = financing.installments.create(
            ordinary=params["ordinary"],
            parcel=params["parcel"],
            paid_parcels=params["paid_parcels"],
            payment_date=params["payment_date"],
            amortization_cents=FinancingServices.convert_to_cents(
                params["amortization_cents"]
            ),
            interest_cents=FinancingServices.convert_to_cents(params["interest_cents"]),
            insurance_cents=FinancingServices.convert_to_cents(
                params["insurance_cents"]
            ),
            fees_cents=FinancingServices.convert_to_cents(params["fees_cents"]),
            monetary_correction_cents=FinancingServices.convert_to_cents(
                params["monetary_correction_cents"]
            ),
            adjustment_cents=FinancingServices.convert_to_cents(
                params["adjustment_cents"]
            ),
        )
        return installment
